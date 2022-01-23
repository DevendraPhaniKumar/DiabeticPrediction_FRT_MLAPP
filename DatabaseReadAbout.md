The resources for this dataset can be found at https://www.openml.org/d/37

Author: [Vincent Sigillito](vgs@aplcen.apl.jhu.edu)  

Source: [Obtained from UCI](https://archive.ics.uci.edu/ml/datasets/pima+indians+diabetes) 

Please cite: [UCI citation policy](https://archive.ics.uci.edu/ml/citation_policy.html)  

1. Title: Pima Indians Diabetes Database
  
 2. Past Usage:
     1. Smith,~J.~W., Everhart,~J.~E., Dickson,~W.~C., Knowler,~W.~C., &
        Johannes,~R.~S. (1988). Using the ADAP learning algorithm to forecast
        the onset of diabetes mellitus.  In {it Proceedings of the Symposium
        on Computer Applications and Medical Care} (pp. 261--265).  IEEE
        Computer Society Press.
 
        The diagnostic, binary-valued variable investigated is whether the
        patient shows signs of diabetes according to World Health Organization
        criteria (i.e., if the 2 hour post-load plasma glucose was at least 
        200 mg/dl at any survey  examination or if found during routine medical
        care).   The population lives near Phoenix, Arizona, USA.
 
        Results: Their ADAP algorithm makes a real-valued prediction between
        0 and 1.  This was transformed into a binary decision using a cutoff of 
        0.448.  Using 576 training instances, the sensitivity and specificity
        of their algorithm was 76% on the remaining 192 instances.
 
 3. Relevant Information:
       Several constraints were placed on the selection of these instances from
       a larger database.  In particular, all patients here are females at
       least 21 years old of Pima Indian heritage.  ADAP is an adaptive learning
       routine that generates and executes digital analogs of perceptron-like
       devices.  It is a unique algorithm; see the paper for details.
 
 4. Number of Instances: 768
 
 5. Number of Attributes: 8 plus class 
 
 6. For Each Attribute: (all numeric-valued)

 Please note as some of the data is not readily available I have removed two attributes in prediction(Attribute 4,7) 
    1. Number of times pregnant
    2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
    3. Diastolic blood pressure (mm Hg)
    4. Triceps skin fold thickness (mm) // Not used in our prediction
    5. 2-Hour serum insulin (mu U/ml)
    6. Body mass index (weight in kg/(height in m)^2)
    7. Diabetes pedigree function // Not used in our prediction
    8. Age (years)
    9. Class variable (0 or 1)
 
 7. Missing Attribute Values: None
 
 8. Class Distribution: (class value 1 is interpreted as "tested positive for
    diabetes")
 
    Class Value  Number of instances
    0            500
    1            268
 
 9. Brief statistical analysis:
 
     Attribute number:    Mean:   Standard Deviation:
     1.                     3.8     3.4
     2.                   120.9    32.0
     3.                    69.1    19.4
     4.                    20.5    16.0
     5.                    79.8   115.2
     6.                    32.0     7.9
     7.                     0.5     0.3
     8.                    33.2    11.8
 
 Relabeled values in attribute 'class'
    From: 0                       To: tested_negative     
    From: 1                       To: tested_positive