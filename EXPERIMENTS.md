## EXP 1:
Train and evalute NER and SPAN CAT architectures on the same subset of data
### Results:
##### Summary:
| P | R | F | ARCH |
|:-----|:--------:|------:| ------:|
| 0.72 | 0.64 | 0.68 | NER |
| 0.88 | 0.65 | 0.75 | SPAN CAT |

##### Entities Details:

**PERSON**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.63 | 0.47 | 0.54 | NER |
| 0.83 | 0.73 | 0.77 | SPAN CAT |

**DIPLOMA**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.70 | 0.63 | 0.66 | NER |
| 0.87 | 0.34 | 0.49 | SPAN CAT |

**TITLE**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.54 | 0.33 | 0.41 | NER |
| 0.87 | 0.66 | 0.75 | SPAN CAT |

**ADDRESS**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:|
| 0.43 | 0.38 | 0.41 | NER |
| 0.8 | 0.3 | 0.44 | SPAN CAT |

**POSITION**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.62 | 0.57 | 0.60 | NER |
| 0.87 | 0.63 | 0.73 | SPAN CAT |

**ORG**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.56 | 0.51 | 0.54 | NER |
| 0.85 | 0.63 | 0.72 | SPAN CAT |

**INSTITUT**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.60 | 0.57 | 0.60 | NER |
| 0.87 | 0.63 | 0.73 | SPAN CAT |

**LOC**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:|
| 0.82 | 0.76 | 0.79 | NER |
| 0.96 | 0.87 | 0.91 | SPAN CAT |

**SKILL**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.46 | 0.36 | 0.40 | NER |
| 0.58 | 0.36 | 0.44 | SPAN CAT |

**DATE**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.97 | 0.95 | 0.96 | NER |
| 0.98 | 0.98 | 0.98 | SPAN CAT |

**BIRTH/AGE**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:|
| 0.92 | 0.73 | 0.81 | NER |
| 0.0 | 0.0 | 0.0 | SPAN CAT |

## EXP 2:
Train and evalute SPAN CAT architecture with a **distilbert** and **jobbert** on the same subset of data
### Results:
##### Summary:

| P | R | F | ARCH |
|:-----|:--------:|------:| ------:|
| 0.89 | 0.64 | 0.74 | DISTILL-BERT |
| 0.91 | 0.61 | 0.74 | JOBBERT |

##### Entities Details:

**PERSON**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.97 | 0.93 | 0.95 | DISTILL-BERT |
| 0.97 | 0.97 | 0.97 | JOBBERT |

**DIPLOMA**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.71 | 0.26 | 0.38 | DISTILL-BERT |
| 0.81 | 0.23 | 0.36 | JOBBERT |

**TITLE**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.87 | 0.72 | 0.78 | DISTILL-BERT |
| 0.90 | 0.72 | 0.8 | JOBBERT |

**ADDRESS**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:|
| 0.79 | 0.35 | 0.49 | DISTILL-BERT |
| 0.8 | 0.36 | 0.5 | JOBBERT |

**POSITION**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.88 | 0.67 | 0.76 | DISTILL-BERT |
| 0.90 | 0.62 | 0.74 | JOBBERT |

**ORG**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.86 | 0.82 | 0.84 | DISTILL-BERT |
| 0.91 | 0.72 | 0.81 | JOBBERT |

**INSTITUT**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.87 | 0.72 | 0.78 | DISTILL-BERT |
| 0.90 | 0.72 | 0.8 | JOBBERT |

**LOC**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:|
| 0.95 | 0.86 | 0.9 | DISTILL-BERT |
| 0.93 | 0.86 | 0.89 | JOBBERT |

**SKILL**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.83 | 0.74 | 0.83 | DISTILL-BERT |
| 0.87 | 0.78 | 0.82 | JOBBERT |

**DATE**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:| 
| 0.98 | 0.59 | 0.74 | DISTILL-BERT |
| 0.98 | 0.59 | 0.74 | JOBBERT |

**BIRTH/AGE**

| P | R | F | ARCH |
|:-----|:--------:|------:|------:|
| 0.83 | 0.84 | 0.83 | DISTILL-BERT |
| 0.91 | 0.84 | 0.88 | JOBBERT |