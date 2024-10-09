# Range Inputs
S_min = 
S_max = 
T_min = 
T_max = 
wingLoading_min = 
wingLoading_max = 
thrustLoading_min = 
thrustLoading_max = 

# Payload Inputs
nPilots = 2
nFA = 3
wCrew = 1050
nPax = 150
wPax = 190
wBag = 30
wPayload = nPax*(wPax+wBag)

## Constraint and Mission analysis

# Phase 1: Taxi out for 20 min, assuming 10% of takeoff full power fuel flow

# Phase 2: Takeoff and clear a 35-ft obstacle in no greater than 5500 ft with two engines operating at sea level and standard day. Assume takeoff rate of climb at 3000 ft/min

# Phase 3: Climb to 10,000 ft at 250 KEAS with a rate of climb of 3000 ft/min

# Phase 4: Accelerate from 250 KEAS to 290 KEAS at 10,000 ft within 1 minute

# Phase 5: Climb at 290 KEAS with a rate of climb of 3000 ft/min until reaching Mach 0.78

# Phase 6: Continue climb to 35,000 ft at Mach 0.78 with a rate of climb of 1500 ft/min

dVdt = 0
n = 1
r = 0

TW_P6_Climb = (beta/alpha)*((q/B)

# Phase 7: Cruise at 35,000 ft for 3000 nautical miles at Mach 0.78

dhdt = 0
dVdt = 0
n = 1

r = 0
TW_P7_Cruise = 

# Phase 8: Descend from cruise altitude to 3000 ft at 250 KEAS with a rate of descent of 1500 ft/min

# Phase 9: Decelerate from 250 KEAS to an approach speed of 135 KEAS at 3000 ft, assuming no fuel flow

# Phase 10: Approach at 135 KEAS with a descent angle of 3 degrees until sea level, assuming 20% of takeoff full power fuel flow

# Phase 11: Execute missed approach (full power go-around) and climb from sea level to 15,000 ft at 250 KEAS with a rate of climb of 3000 f t/min

# Phase 12: Cruise at 15,000 ft for 200 nautical miles at 250 KEAS to an alternate airport

# Phase 13: Loiter at 15,000 ft for 45 minutes at best endurance speed

# Phase 14: Descend to 3000 ft at 250 KEAS with a rate of descent of 1500 f t/min

# Phase 15: Decelerate from 250 KEAS to an approach speed of 135 KEAS at 3000 ft, assuming no fuel flow

# Phase 16: Approach at 135 KEAS with a descent angle of 3 degrees, assuming 20% of takeoff full power fuel flow

# Phase 17: Land at the alternate airport with a 5% fuel reserve

# Phase 18: Taxi in for 20 min, assuming 10% of takeoff full power fuel flow.

## Additional constraints

# Maintain a gradient of climb no less than 5% with one engine inoperative after clearing the 35-ft obstacle during takeoff

# Maintain a rate of climb no less than 300 f t/min with two engines at a service ceiling of 41,000 ft with cruise Mach number (0.78) and the weight at the top of climb (35,000 ft)

# Achieve a maximum Mach number of 0.82 in level flight at cruise altitude with the weight at the top of climb

# Sustain a 45-deg banked steep turn at 39,000 ft with cruise Mach number

# Approach constraint should be evaluated at the maximum landing weight, assumed as 85% maximum ramp weight