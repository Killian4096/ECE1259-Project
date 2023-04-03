%clc, clear, close all
j = 1i;
relative_permitivity_list = [1, 2.1, 2.56, 3.8, 5.4, 10];
dielectric_strength_list = [3e6, 60e6, 20e6, 30e6, 200e6, 30e6];
conductivity_list = [0, 10e-15, 10e-17, 10e-17, 10e-15, 10e-12];
frequency = {1*10^-16, 100*10^6}


%Caller user input script
values = get_user_input();

%Generate values from user inputs
relative_permitivity = relative_permitivity_list(values(1));
dielectric_strength = dielectric_strength_list(values(1));
area = values(2);
distance = values(3);
capacitance = find_capacitance(dielectric_strength, area, distance);
breakdownvoltage = find_breakdownvoltage(dielectric_strength_list(values(1)), distance);
conductivity = conductivity_list(values(1));

%Print Static Values
fprintf('C = %f nF\n', capacitance);
fprintf('V_BR = %f V\n', breakdownvoltage);

%Generate Graphs
graphinfo(conductivity, relative_permitivity, capacitance, frequency)


function values = get_user_input()
    %displays list of dielectrics and their permitivities
    dielectric_constants = containers.Map([1, 2, 3, 4, 5, 6],...
    {'Air, εᵣ = 1.00', 'Teflon, εᵣ = 2.10', 'Polystyrene, εᵣ = 2.56',...
     'Quartz(fused), εᵣ = 3.8', 'Mica, εᵣ = 5.40', 'Glass, εᵣ = 10.0'});
    fprintf("\nAvailable Dielectrics:\n");
    for i = 1:length(dielectric_constants)
        fprintf("(%d) %s\n", i, dielectric_constants(i));
    end
    %Get user data
    userInput = input("Select your dielectric(number), choose the area of the capacitor's plates(m), and the distance between the plates(mm):\n", 's');
    data = regexp(userInput, '\d+(\.\d+)?', 'match'); % removes common unwanted inputs
    values = str2double(data);
    while(length(values) ~= 3) % error checking for invalid input
        if (length(values)<3)
            fprintf("Invalid input. Only enter numbers separated by some delimiter.\n");
            displayDielectrics(dielectric_constants);
            userInput = input("Select your dielectric(number), choose the area of the capacitor's plates(m), and the distance between the plates(mm):\n", 's');
            data = regexp(userInput, '\d+(\.\d+)?', 'match');
            values = str2double(data);
        else
            fprintf("Too many inputs. Only enter numbers corresponding to the dielectric, area, and separation_distance.\n");
            displayDielectrics(dielectric_constants);
            userInput = input("Select your dielectric(number), choose the area of the capacitor's plates(m), and the distance between the plates(mm):\n", 's');
            data = regexp(userInput, '\d+(\.\d+)?', 'match');
            values = str2double(data);
        end
    end
end

function capacitance = find_capacitance(p, a, d)
            % permitivity, area, distance
            capacitance = p*8.854*10^-12*a*10^4/(d*10^-3);
end

function bdv = find_breakdownvoltage(E, d)
    % E = dielectric strength
    bdv = E*d*10^-3; % breakdown voltage
end

function graphinfo(conductivity, relative_perm, capacitance, frequency)
    p = 8.854*10^-12*relative_perm; % permitivity
    
    subplot(2, 1, 1);
    %x = linspace(0, 100, 100);
    %y1 = tan(conductivity./(x*10^6*p));
    sys1 = tf([capacitance, conductivity],1);
    bodeplot(sys1, frequency)
    title("Leakage Current")
    
    subplot(2, 1, 2);
    %x = linspace(0, 100, 100);
    %y2 = 1./(x*capacitance);
    sys1 = tf([capacitance./conductivity, 1],[capacitance]);
    bodeplot(sys1, frequency)
    title('Capacitive Reactance');

end

%{
function Display(arr1, arr2)
    fprintf('You created these capacitors\n');
    for i = 1:length(arr1)
        disp(['Capacitor #', num2str(i), ': capacitance = ',... 
              num2str(arr1(i)), ' nF, V_BR = ', num2str(arr2(i)) ' V'])
    end
end
%}
