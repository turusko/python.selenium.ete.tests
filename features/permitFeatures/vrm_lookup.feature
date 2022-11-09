@permit
Feature: User is able to lookup VRM
      
      User is able to perform a lookup on their vehicle and confirm that their vehicle has been found
        @fixture.vrm.lookup
        Scenario Outline: Vehicle lookup returns correct make and colour
             When user looksup <vrm>
             Then vehicle colour is displayed as <colour>
              And vehicle make is displayed as <make>

        Examples: vehicles
                  | vrm   | colour | make   |
                  | t2omf | black  | jaguar |
                  | taw1  | silver | mini   |
             
        @fixture.vrm.lookup
        Scenario Outline: Invalid VRM gets error message
             When user looksup invalid <vrm>
             Then error message is displayed as <message>

        Examples: vehicles
                  | vrm                                  | message                                                                                                                 |
                  | asdddddddddddddddddddddddddddddddddd | Your vehicle registration is too long. vehicle registration must not exceed 23 characters                               |
                  | £                                    | Your vehicle registration contains invalid characters. Vehicle registration should only contain alphanumeric characters |
                  | *                                    | Your vehicle registration contains invalid characters. Vehicle registration should only contain alphanumeric characters |
                  | ^                                    | Your vehicle registration contains invalid characters. Vehicle registration should only contain alphanumeric characters |
                  | %                                    | Your vehicle registration contains invalid characters. Vehicle registration should only contain alphanumeric characters |
                  | &                                    | Your vehicle registration contains invalid characters. Vehicle registration should only contain alphanumeric characters |
