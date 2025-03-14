from python_venv.fiche_perso import generate_character, display_character

def test_generate_character():
    character, Sorts, Sorts_Couts = generate_character()

    assert isinstance(character, dict)

    required_keys = ["Nom", "Race", "Classe", "Force", "Dextérité", "Constitution", "Intelligence", "Sagesse", "Charisme", "Historique"]
    for key in required_keys:
        assert key in character

    assert isinstance(Sorts, dict)
    assert len(Sorts) == 5

    assert isinstance(Sorts_Couts, dict)
    assert len(Sorts_Couts) == 5

    for cost in Sorts_Couts.values():
        assert isinstance(cost, int)
        assert 1 <= cost <= 10

def test_display_character(capsys):
    character, Sorts, Sorts_Couts = generate_character()
    display_character(character, Sorts, Sorts_Couts)

    captured = capsys.readouterr()
    output = captured.out

    for key, value in character.items():
        assert f"{key}: {value}" in output

    for key, value in Sorts.items():
        assert f"{key}: {value}" in output

    for key, value in Sorts_Couts.items():
        assert f"{key}: {value}" in output