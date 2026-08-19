class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {

        // For each row, store a bitmask representing the reserved seats
        unordered_map<int, int> rows;

        // Build the bitmask for each row
        for (auto& seat : reservedSeats) {
            int row = seat[0];
            int s = seat[1];

            // Seat 1 -> bit 0
            // Seat 2 -> bit 1
            // ...
            // Seat 10 -> bit 9
            rows[row] |= (1 << (s - 1));
        }

        // Bitmasks for the three possible groups of 4 seats
        //
        // LEFT   = seats 2, 3, 4, 5
        // MIDDLE = seats 4, 5, 6, 7
        // RIGHT  = seats 6, 7, 8, 9

        int LEFT   = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4);
        int MIDDLE = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6);
        int RIGHT  = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8);

        // Every row without any reserved seat can fit 2 families
        long long ans = 2LL * (n - rows.size());

        // Process only rows that contain reserved seats
        for (auto& [row, reserved] : rows) {

            // If both LEFT and RIGHT areas are available,
            // we can fit two families
            if ((reserved & LEFT) == 0 &&
                (reserved & RIGHT) == 0) {

                ans += 2;
            }

            // Otherwise, if at least one of the three areas is available,
            // we can fit one family
            else if ((reserved & LEFT) == 0 ||
                     (reserved & MIDDLE) == 0 ||
                     (reserved & RIGHT) == 0) {

                ans += 1;
            }
        }

        return ans;
    }
};