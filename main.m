clc
j = 1i;
dielectric_constants = containers.Map([1, 2, 3, 4, 5],... 
{'Air, εᵣ = 1.00', 'Teflon, εᵣ = 2.10', 'Polyethylene, εᵣ = 2.26',... 
 'Mica, εᵣ = 5.40', 'Glass, εᵣ = 10.0'});
relative_permitivity = [1, 2.1, 2.26, 5.4, 10];
dielectric_strength = [3e6, 60e6, 47e6, 200e6, 30e6];
conductivity = [0, 1e-15, 1e-16, 1e-15, 1e-12];

%calling functions
GraphLossTangent(1e-12, 10, 143e-9);
displayDielectrics(dielectric_constants);
[caps, bdvs] = inputScript(relative_permitivity, dielectric_strength);
Display(caps, bdvs);

function displayDielectrics(dielectric_constants)
    %displays list of dielectrics and their permitivities
    fprintf("\nAvailable Dielectrics:\n");
    for i = 1:length(dielectric_constants)
        fprintf("(%d) %s\n", i, dielectric_constants(i));
    end
end

function [caps, bdvs] = inputScript(relative_permitivity, dielectric_strength)
    caps = []; % stores all the capacitances from the user created capacitors
    bdvs = []; % stores all break down voltages from the user created capacitors
    flag = true; % checks if user still wants to design capacitors
    while(flag == true)
        userInput = input("Select your dielectric(number), choose the area of the capacitor's plates(cm), and the distance between the plates(mm):\n", 's');
        data = regexp(userInput, '\d+(\.\d+)?', 'match'); % removes common unwanted inputs
        values = str2double(data);
        while(length(values) ~= 3) % error checking for invalid input
            if (length(values)<3)
                fprintf("Invalid input. Only enter numbers separated by some delimiter.\n");
                displayDielectrics(dielectric_constants);
                userInput = input("Select your dielectric(number), choose the area of the capacitor's plates(cm), and the distance between the plates(mm):\n", 's');
                data = regexp(userInput, '\d+(\.\d+)?', 'match');
                values = str2double(data);
            else
                fprintf("Too many inputs. Only enter numbers corresponding to the dielectric, area, and separation_distance.\n");
                displayDielectrics(dielectric_constants);
                userInput = input("Select your dielectric(number), choose the area of the capacitor's plates(cm), and the distance between the plates(mm):\n", 's');
                data = regexp(userInput, '\d+(\.\d+)?', 'match');
                values = str2double(data);
            end
        end
        
        dielectric = relative_permitivity(values(1));
        area = values(2);
        distance = values(3);
        
        capacitance = Capacitance(dielectric, area, distance);
        caps(end+1) = capacitance; % adds 'n' capacitance to caps list
        bdv = BreakdownVoltage(dielectric_strength(values(1)), distance);
        bdvs(end+1) = bdv; % adds 'n' breakdown voltage to bdvs list 
        userInput = input("Would you like to create another capacitor(Y/N)? ", 's');
        if (strcmpi(userInput, 'Y'))
            flag = true;
        else
            flag = false;
        end
        fprintf('\n');
    end
end

function capacitance = Capacitance(p, a, d)
            % permitivity, area, distance
            capacitance = p*8.854*10^-12*a*10^9/(d*10^-3);
            fprintf('C = %f nF\n', capacitance);
end

function bdv = BreakdownVoltage(E, d)
    % E = dielectric strength
    bdv = E*d*10^-3; % breakdown voltage
    fprintf('V_BR = %f V\n', bdv);
end

function GraphLossTangent(conductivity, relative_perm, capacitance)
    p = 8.854*10^-12*relative_perm; % permitivity
    
    subplot(2, 1, 1);
    x = linspace(0, 100, 100);
    y1 = tan(conductivity./(x*10^6*p));
    plot(x, y1)
    xlabel('Frequency(Mhz)');
    ylabel('Loss Tangent');
    
    subplot(2, 1, 2);
    x = linspace(0, 100, 100);
    y2 = 1./(x*capacitance);
    plot(x, y2)
    xlabel('Frequency(Mhz)');
    ylabel('Capacitive Reactance');
    
end


function Display(arr1, arr2)
    fprintf('You created these capacitors\n');
    for i = 1:length(arr1)
        disp(['Capacitor #', num2str(i), ': capacitance = ',... 
              num2str(arr1(i)), ' nF, V_BR = ', num2str(arr2(i)) ' V'])
    end
end


        
