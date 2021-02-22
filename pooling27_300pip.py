from opentrons import labware, robot, instruments

pool_dict = {'X1': ['A1'],
 'X2': ['B1'],
 'X3': ['C1'],
 'Y1': ['A2'],
 'Y2': ['B2'],
 'Y3': ['C2'],
 'Z1': ['A3'],
 'Z2': ['B3'],
 'Z3': ['C3']}

slice_dict = {'X1': ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'A2'],
 'X2': ['B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'A3', 'B3'],
 'X3': ['C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'A4', 'B4', 'C4'],
 'Y1': ['A1', 'B1', 'C1', 'B2', 'C2', 'D2', 'C3', 'D3', 'E3'],
 'Y2': ['D1', 'E1', 'F1', 'E2', 'F2', 'G2', 'F3', 'G3', 'H3'],
 'Y3': ['G1', 'H1', 'A2', 'H2', 'A3', 'B3', 'A4', 'B4', 'C4'],
 'Z1': ['A1', 'D1', 'G1', 'B2', 'E2', 'H2', 'C3', 'F3', 'A4'],
 'Z2': ['B1', 'E1', 'H1', 'C2', 'F2', 'A3', 'D3', 'G3', 'B4'],
 'Z3': ['C1', 'F1', 'A2', 'D2', 'G2', 'B3', 'E3', 'H3', 'C4']}

#robot.connect()

#custom_plate_name = 'tulio96'
#labware.create('tulio96', grid=(12, 8), spacing=(8.3, 8.3), diameter=8.3, depth=42, volume=2000)


custom_plate_name = 'tulio96'
if custom_plate_name not in labware.list(): 
    labware.create(
        custom_plate_name, 
        grid=(12, 8), 
        spacing=(8.3, 8.3), 
        diameter=8.3, 
        depth=42, 
        volume=2000)
    
# name of you labware
# number of (columns, rows)
# distances (mm) between each (column, row)
# diameter (mm) of each well
# depth (mm) of each well
# volume (μL) of each well

tiprack = labware.load('opentrons-tiprack-300ul', slot='1')
pool_source = labware.load('tulio96', '7')
pool_slice  = labware.load('tulio96', '10')
trash = labware.load('trash-box', '12', share=True)
pipette = instruments.P300_Single(mount='right', tip_racks=[tiprack], trash_container=trash)

for pool in pool_dict.keys():
    for single_slice in slice_dict[pool]:
        pipette.pick_up_tip()
        pipette.transfer(200,pool_source.wells(single_slice),pool_slice.wells(pool_dict[pool][0]))
        #pipette.drop_tip(trash)