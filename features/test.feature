@permit
Feature: User is able to lookup VRM

        @fixture.vrm.lookup
        Scenario Outline: Adding numbers
             When user looksup <vrm>
             Then vehicle colour is displayed as <colour>
              And vehicle make is displayed as <make>

        Examples: vehicles
                  | vrm   | colour | make   |
                  | t2omf | black  | jaguar |
                  | taw1  | silver | mini   |
             


