clc,clear, close all;
%% System Parameter
L = 50*1e-6;            % Inductivity
R_L = 750e-3;           % Internal Inductivity Resistance
R_DS = 50e-3;           % Drain-Source Resistance
R = 500;                % Load Resistance
C = 330e-6;             % Capacity
U_0 = 100;              % Source Voltage
t = 1e-3*[0,2,3,5,10];
D = [0.1,0.2,0.3,0.4,0.5];
U_C0 = 0;    % Inital Capacity Voltage
%% DCDC Parameter
frequency = 100e3;      % Switching Frequency
%% Simulation Setup
t_sim =  1000/frequency;
t_step = 0.001/frequency;
model = 'Boost_Converter_Model';
load_system(model);
sim(model,t_sim);
Boost_Converter_Plot
