include "sfc-3.dzn";

enum K = {UPF, APP};

int: Max_Delay_For_App; %| formulation: D_max

array[NODES, NODES] of int: delay;  % Delay between nodes | formulation: D
array[NODES] of int: capacity;    % Max capacity for each node | formulation: C
array[NODES, NODES] of int: transmission_cost;  % Transmission cost between nodes | formulation: T_cost
array[NODES] of int: Request_Array;    % Nr of user requests per node | formulation: R_A


% Decision variables
array[V, K] of var 0.. : x; % non negative  - V = Node na ktorym jest UPF lub apka  K = App_type
array[A, K, V, V] of var 0..1000 : y; % non negative  - A zrodla zadania, k = App_type, V = nr wezla UPF, V = nr wezla aplikacji

%Constraints 

% Warunek na rozpływ ruchu - naplywajacy ruch zostanie przekierowany do odpowiednich wezlow, caly ruch obsluzony
constraint forall(a in A, k in K where k!=UPF)(sum(v in V, u in V)(y[a, k, v, u]) >= Request_Array[a]);

%Dla nie UPF aplikacja na wezle uruchomiona wieksza niz ruch, z ktorego wychodzi
constraint forall(u in V, k in K where k!=UPF)(sum(a in A, v in V)(y[a, k, v, u]) <= x[u,APP]);

%dla UPF ilosc zasobow x > y - Suma ruchu idacego przez wezel musi byc mniejsza lub rowna niz zdolnosc obliczeniowa ilosci uruchomionych na tym wezle UPF-ow
constraint forall(v in V)(sum(a in A, k in K, u in V)(y[a, k, v, u]) <= x[v,UPF]);

% Zasoby w wezlach musza byc wieksze niz ilosc uruchomionych na nich i UPF i Apek
constraint forall(n in NODES)(capacity[n] >= (x[n,UPF] + x[n,APP]));


% Opoznienia musza byc mniejsze niz w requescie. Suma opoznien na laczach przez ktore idzie trasa (delay App - UPF + delay Upf + zrodlo) < max akceptowalny dla requestu
constraint forall(a in A, k in K where k!=UPF, v in V, u in V where y[a, k, v, u] > 0)( delay[a,v]+delay[v,u] <= Max_Delay_For_App);


% Variables
var int: total_placement_cost = sum(n in NODES)(x[n,UPF]+x[n,APP]);
var int: total_transmission_cost = sum(a in A, k in K where k!=UPF, v in V, u in V where y[a, k, v, u] > 0)( transmission_cost[a,v]+transmission_cost[v,u]);
var int: total_cost = total_placement_cost + total_transmission_cost;


solve minimize total_cost; %| formulation: f

% Output the results

output ["Total cost: \(total_cost) \n"];
output ["Placement cost: \(total_placement_cost) \n"];
output ["Transmission cost: \(total_transmission_cost) \n"];


output ["Placement array: \n"];

output [show2d(x)];

output ["\n Source, App_Type, Upf_Node_Nr, App_Node_Nr: \n"];
%output ["\(a) \(k) \(v) \(u) | \(y[a,k,v,u]) \n" | a in A, k in {UPF, APP}, v in V, u in V];
output ["\(a) \(k) \(v) \(u) | \(y[a,k,v,u]) \n" | a in A, k in {UPF, APP}, v in V, u in V where fix(y[a,k,v,u] != 0)];
