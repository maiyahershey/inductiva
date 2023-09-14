"""Test for MachineGroup class."""
import inductiva


def test_machine_group_start(mg: inductiva.resources.MachineGroup):

    mg.start()

    # When the machine group is successfully started, it returns
    # a name of that group. So if the name exists the machine group
    # was created without any errors.
    assert mg.name is not None


def test_get_machine_groups(mg: inductiva.resources.MachineGroup):
    machine_groups = inductiva.resources.machine_groups.get()

    assert len(machine_groups) > 0
    assert machine_groups[0].name == mg.name
    assert machine_groups[0].machine_type == mg.machine_type
    assert machine_groups[0].num_machines == mg.num_machines
    assert machine_groups[0].spot == mg.spot
    assert machine_groups[0].disk_size_gb == mg.disk_size_gb
    assert machine_groups[0].zone == mg.zone


def test_machine_groups_cost(mg: inductiva.resources.MachineGroup):
    cost = mg.estimate_cloud_cost()

    # Since we don't have a proper way to test if the printed cost is right,
    # here, only if the cost is returned checked.
    assert cost > 0


def test_machine_group_termination(mg: inductiva.resources.MachineGroup):
    mg.terminate()
    machine_groups = inductiva.resources.machine_groups.get_all()

    # If the machine group was successfully terminated, the list of machine
    # groups should be empty.
    assert len(machine_groups) == 0


def test_machine_group():
    """Test the MachienGroup obect methods.

    All the methods to be tested are grouped in this function, so that the
    machine group is only created once and all the tests are ran with it."""
    mg = inductiva.resources.MachineGroup(machine_type="c2-standard-4",
                                          num_machines=2,
                                          spot=True,
                                          disk_size_gb=50)

    try:
        test_machine_group_start(mg)
        test_get_machine_groups(mg)
        test_machine_groups_cost(mg)
        test_machine_group_termination(mg)

    except AssertionError as e:
        # If any error occured, the machine group is terminated in order not to
        # leave any machine group running while debugging.
        mg.terminate()
        raise e
