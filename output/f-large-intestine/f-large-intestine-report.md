## 3D Reference Organ Validation Report

### Reverted relationship

| user_olabel                                          | user_slabel                                                                     | o              | s              | olabel                   | slabel           |
|------------------------------------------------------|---------------------------------------------------------------------------------|----------------|----------------|--------------------------|------------------|
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_descending_colon         | UBERON:0001158 | UBERON:0001159 | descending colon         | sigmoid colon    |
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_splenic_flexure_of_colon | UBERON:0022276 | UBERON:0001158 | splenic flexure of colon | descending colon |
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_splenic_flexure_of_colon | UBERON:0022276 | UBERON:0001157 | splenic flexure of colon | transverse colon |

### Redundant relationship

| user_olabel                                          | user_slabel                                                                     | o              | s              | olabel                   | slabel          |
|------------------------------------------------------|---------------------------------------------------------------------------------|----------------|----------------|--------------------------|-----------------|
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_descending_colon         | UBERON:0001158 | UBERON:0001052 | descending colon         | rectum          |
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_hepatic_flexure_of_colon | UBERON:0022277 | UBERON:0001156 | hepatic flexure of colon | ascending colon |

### Overlaps relationship

| user_olabel                                          | user_slabel                                                             | o              | s              | olabel           | slabel                   |
|------------------------------------------------------|-------------------------------------------------------------------------|----------------|----------------|------------------|--------------------------|
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_transverse_colon | UBERON:0001157 | UBERON:0022277 | transverse colon | hepatic flexure of colon |
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_ascending_colon  | UBERON:0001156 | UBERON:0022277 | ascending colon  | hepatic flexure of colon |

#### Overlaps and reverted relationship

| user_olabel                                          | user_slabel                                                                     | o              | s              | olabel                   | slabel           |
|------------------------------------------------------|---------------------------------------------------------------------------------|----------------|----------------|--------------------------|------------------|
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_splenic_flexure_of_colon | UBERON:0022276 | UBERON:0001158 | splenic flexure of colon | descending colon |
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_splenic_flexure_of_colon | UBERON:0022276 | UBERON:0001157 | splenic flexure of colon | transverse colon |

### Require curation

| user_olabel                                          | user_slabel                                                             | o              | s              | olabel           | slabel          |
|------------------------------------------------------|-------------------------------------------------------------------------|----------------|----------------|------------------|-----------------|
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_ileocecal_valve  | UBERON:0000569 | UBERON:0001153 | ileocecal valve  | caecum          |
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_ileocecal_valve  | UBERON:0000569 | UBERON:0001156 | ileocecal valve  | ascending colon |
| ccf:VHFLargeIntestine | ccf:VHFemaleOrgans_VH_F_transverse_colon | UBERON:0001157 | UBERON:0001153 | transverse colon | caecum          |
