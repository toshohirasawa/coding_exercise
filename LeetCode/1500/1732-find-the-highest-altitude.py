class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude, highest_altitude = 0, 0
        for i in range(len(gain)):
            altitude += gain[i]
            highest_altitude = max(altitude, highest_altitude)
        return highest_altitude
