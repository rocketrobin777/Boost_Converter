/*@author: robin leuering*/

#include <stdio.h>

/*Differential equations*/

float current_calc(float U0,float UC,float I,float D,float L,float RL,float RDS,float dt){
    float dI = (U0-(D*RDS+RL)*I-(1-D)*UC)/L;    // Calc current slope
    return I+dI*dt;                             // Calc current  
}

float voltage_calc(float UC,float I,float C, float R, float dt){
    float dUC = (I-UC/R)/C;                     // Calc voltage slope
    return UC+dUC*dt;                           // Calc voltage
}

/*Time conditions*/

#define tsim 0.005          // Simulation duration
#define n 200               // Number of time steps

/*System parameters*/

#define L 0.00005           // Inductivity
#define RL 0.750            // Internal inductor resistance
#define RDS 0.05            // Drain-Source resistance
#define R 500.0             // Load resistance
#define C 0.000330          // Capacity
#define D 0.50              // Duty cycle
#define U0 100.0            // Source Voltage

/*System values*/

float I[n];                 // Current vector
float UC[n];                // Voltage vector
float t[n];                 // Time vector
float dt = tsim/n;          // Simulation step time

/*Solve System*/
int main(){
    t[0]    = 0;            // Initialize time
    I[0]    = 0;            // Initialize current
    UC[0]   = U0;           // Initialize voltage
    printf ("t,        I,         UC,\n");
    for(int i = 1; i < n; i++)
        {
          t[i]  = t[i-1]+dt;
          I[i]  = current_calc(U0,UC[i-1],I[i-1],D,L,RL,RDS,dt);
          UC[i] = voltage_calc(UC[i-1],I[i],C,R,dt);
          printf ("%f, %f, %f,\n",t[i],I[i],UC[i]);
        }
    return 0;
}
