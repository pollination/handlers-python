import json
import os

from pollination_handlers.inputs.simulation import energy_sim_par_to_json, \
    list_to_additional_idf
from honeybee_energy.simulation.parameter import SimulationParameter


def test_energy_sim_par_str():
    res = energy_sim_par_to_json('./tests/assets/simulation_par_simple.json')
    assert res.replace('\\', '/').endswith('tests/assets/simulation_par_simple.json')


def test_energy_sim_par_object():
    with open('./tests/assets/simulation_par_simple.json') as sp:
        data = sp.read()
    data = json.loads(data)
    sim_par = SimulationParameter.from_dict(data)

    res = energy_sim_par_to_json(sim_par)
    assert os.path.isfile(res)


def test_list_to_additional_idf():
    add_text = [
        'Output:Variable, Window_0, Surface Window System Solar Transmittance, Timestep;'
    ]
    res = list_to_additional_idf(add_text)
    assert res.endswith('.idf')
    assert os.path.isfile(res)
