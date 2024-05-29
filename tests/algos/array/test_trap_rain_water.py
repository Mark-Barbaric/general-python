from src.algos.array.trapping_rain_water import trap_rain_water, trap_rain_water_dp


def test_trap_rain_water():
    heights = [0, 1, 0]
    ans = trap_rain_water(heights)
    assert ans == 0
    heights = [0, 2, 1, 0, 1, 3, 2, 2, 0]
    ans = trap_rain_water(heights)
    assert ans == 4


def test_trap_rain_water_dp():
    heights = [0, 1, 0]
    ans = trap_rain_water_dp(heights)
    assert ans == 0
    heights = [0, 2, 1, 0, 1, 3, 2, 2, 0]
    ans = trap_rain_water_dp(heights)
    assert ans == 4
