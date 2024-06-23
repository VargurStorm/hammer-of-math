import csv
from time import time
import numpy as np

import cProfile
import pstats

from core import *
from core.units import *
from simulation.sim import run_multiple_simulations_for_average


def main():
    run_count = 2000

    # Initialize results as a NumPy array
    results = np.empty((0, 11), dtype=object)

    def record_results(attacker_desc, meq_sim, ork_sim, teq_sim, veq_sim, geq_sim):
        new_result = np.array([[
            attacker_desc,
            round(meq_sim.total_damage_not_fnp / run_count, 1),
            round(meq_sim.models_killed / run_count, 1),
            round(ork_sim.total_damage_not_fnp / run_count, 1),
            round(ork_sim.models_killed / run_count, 1),
            round(teq_sim.total_damage_not_fnp / run_count, 1),
            round(teq_sim.models_killed / run_count, 1),
            round(veq_sim.total_damage_not_fnp / run_count, 1),
            round(veq_sim.models_killed / run_count, 1),
            round(geq_sim.total_damage_not_fnp / run_count, 1),
            round(geq_sim.models_killed / run_count, 1)
        ]], dtype=object)
        nonlocal results
        results = np.vstack((results, new_result))

    attacker_1 = [(custodian_guard, 1)]
    meq_sim_1 = run_multiple_simulations_for_average(run_count, Scenario(attacker_1, (meq, 50)))
    ork_sim_1 = run_multiple_simulations_for_average(run_count, Scenario(attacker_1, (oeq, 50)))
    teq_sim_1 = run_multiple_simulations_for_average(run_count, Scenario(attacker_1, (teq, 50)))
    veq_sim_1 = run_multiple_simulations_for_average(run_count, Scenario(attacker_1, (veq, 50)))
    geq_sim_1 = run_multiple_simulations_for_average(run_count, Scenario(attacker_1, (geq, 50)))
    record_results("Custodian Guard", meq_sim_1, ork_sim_1, teq_sim_1, veq_sim_1, geq_sim_1)

    attacker_2 = [(custodian_guard_sustained, 1)]
    meq_sim_2 = run_multiple_simulations_for_average(run_count, Scenario(attacker_2, (meq, 50)))
    ork_sim_2 = run_multiple_simulations_for_average(run_count, Scenario(attacker_2, (oeq, 50)))
    teq_sim_2 = run_multiple_simulations_for_average(run_count, Scenario(attacker_2, (teq, 50)))
    veq_sim_2 = run_multiple_simulations_for_average(run_count, Scenario(attacker_2, (veq, 50)))
    geq_sim_2 = run_multiple_simulations_for_average(run_count, Scenario(attacker_2, (geq, 50)))
    record_results("Custodian Guard with Sustained Hits", meq_sim_2, ork_sim_2, teq_sim_2, veq_sim_2, geq_sim_2)

    attacker_3 = [(custodian_guard_lethal, 1)]
    meq_sim_3 = run_multiple_simulations_for_average(run_count, Scenario(attacker_3, (meq, 50)))
    ork_sim_3 = run_multiple_simulations_for_average(run_count, Scenario(attacker_3, (oeq, 50)))
    teq_sim_3 = run_multiple_simulations_for_average(run_count, Scenario(attacker_3, (teq, 50)))
    veq_sim_3 = run_multiple_simulations_for_average(run_count, Scenario(attacker_3, (veq, 50)))
    geq_sim_3 = run_multiple_simulations_for_average(run_count, Scenario(attacker_3, (geq, 50)))
    record_results("Custodian Guard with Lethal Hits", meq_sim_3, ork_sim_3, teq_sim_3, veq_sim_3, geq_sim_3)

    attacker_4 = [(custodian_guard_lethal_and_sustained, 1)]
    meq_sim_4 = run_multiple_simulations_for_average(run_count, Scenario(attacker_4, (meq, 50)))
    ork_sim_4 = run_multiple_simulations_for_average(run_count, Scenario(attacker_4, (oeq, 50)))
    teq_sim_4 = run_multiple_simulations_for_average(run_count, Scenario(attacker_4, (teq, 50)))
    veq_sim_4 = run_multiple_simulations_for_average(run_count, Scenario(attacker_4, (veq, 50)))
    geq_sim_4 = run_multiple_simulations_for_average(run_count, Scenario(attacker_4, (geq, 50)))
    record_results("Custodian Guard with Lethal Hits and Sustained Hits", meq_sim_4, ork_sim_4, teq_sim_4, veq_sim_4,
                   geq_sim_4)

    with open('simulation_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Attacker', 'Space Marines Damage', 'Space Marines Killed', 'Orks Damage', 'Orks Killed',
                      'Terminators Damage', 'Terminators Killed', 'Vehicles Damage', 'Vehicles Killed', 'Guard Damage',
                      'Guard Killed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow({
                'Attacker': result[0],
                'Space Marines Damage': result[1],
                'Space Marines Killed': result[2],
                'Orks Damage': result[3],
                'Orks Killed': result[4],
                'Terminators Damage': result[5],
                'Terminators Killed': result[6],
                'Vehicles Damage': result[7],
                'Vehicles Killed': result[8],
                'Guard Damage': result[9],
                'Guard Killed': result[10]
            })


if __name__ == "__main__":
    start_time = time()

    # profiler = cProfile.Profile()
    # profiler.enable()

    main()
    print(f"Simulation took {time() - start_time} seconds")
    # profiler.disable()

    #
    # with open('profile_results.txt', 'w') as f:
    #     ps = pstats.Stats(profiler, stream=f)
    #     ps.strip_dirs().sort_stats('cumulative').print_stats(50)
    #
    # ps = pstats.Stats(profiler)
    # ps.strip_dirs().sort_stats('cumulative').print_stats(75)
