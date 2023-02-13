#!/usr/bin/python3

import pymatgen as pg
import sys
import numpy as np

element_properties = {
                     "Ti":{"VEC":4},
                     "Zr":{"VEC":4},
                     "Hf":{"VEC":4},
                     "V":{"VEC":5},
                     "Nb":{"VEC":5},
                     "Ta":{"VEC":5},
                     "Mo":{"VEC":6},
                     "W":{"VEC":6},
                     "Re":{"VEC":7},
                     "Ru":{"VEC":8}
                     }                  

B2_properties = {
  'TiTi': {
    'half bond': 1.4052370606386055,
  'd band bimodality': 0.05774533},
 'TiZr': {
  'half bond': 1.4806357547670252,
  'd band bimodality': 0.061610414},
 'TiHf': {
  'half bond': 1.4722627596459863,
  'd band bimodality': 0.066277572},
 'TiV': {
  'half bond': 1.3492900375384898,
  'd band bimodality': 0.066351391},
 'TiNb': {
  'half bond': 1.4124820911065668,
  'd band bimodality': 0.037946155},
 'TiTa': {
  'half bond': 1.4163657985472158,
  'd band bimodality': 0.052913783},
 'TiMo': {
  'half bond': 1.371065747735163,
  'd band bimodality': 0.056147935},
 'TiW': {
  'half bond': 1.376170979651201,
  'd band bimodality': 0.041728446},
 'TiRe': {
  'half bond': 1.349085709741297,
  'd band bimodality': 0.059897259},
 'TiRu': {
  'half bond': 1.3355601021700063,
  'd band bimodality': 0.049588559},
 'ZrTi': {
  'half bond': 1.4806357547670252,
  'd band bimodality': 0.068861291},
 'ZrZr': {
  'half bond': 1.5497333441846008,
  'd band bimodality': 0.044520128},
 'ZrHf': {
  'half bond': 1.541726785958287,
  'd band bimodality': 0.060876518},
 'ZrV': {
  'half bond': 1.433548576418533,
  'd band bimodality': 0.069456667},
 'ZrNb': {
  'half bond': 1.4882610287873488,
  'd band bimodality': 0.057224622},
 'ZrTa': {
  'half bond': 1.492051456329931,
  'd band bimodality': 0.067938795},
 'ZrMo': {
  'half bond': 1.45111928111061,
  'd band bimodality': 0.066036345},
 'ZrW': {
  'half bond': 1.4560409142592914,
  'd band bimodality': 0.070652417},
 'ZrRe': {
  'half bond': 1.4316089436393356,
  'd band bimodality': 0.059402707},
 'ZrRu': {
  'half bond': 1.4209513274152474,
  'd band bimodality': 0.035840283},
 'HfTi': {
  'half bond': 1.4722627596459863,
  'd band bimodality': 0.065427657},
 'HfZr': {
  'half bond': 1.541726785958287,
  'd band bimodality': 0.060148969},
 'HfHf': {
  'half bond': 1.5336828058095522,
  'd band bimodality': 0.05413918},
 'HfV': {
  'half bond': 1.4224438084558815,
  'd band bimodality': 0.07357842},
 'HfNb': {
  'half bond': 1.4786220901348968,
  'd band bimodality': 0.077152764},
 'HfTa': {
  'half bond': 1.482545774915564,
  'd band bimodality': 0.068429843},
 'HfMo': {
  'half bond': 1.439676927855975,
  'd band bimodality': 0.068606235},
 'HfW': {
  'half bond': 1.4440507258597126,
  'd band bimodality': 0.074584289},
 'HfRe': {
  'half bond': 1.4187570251826924,
  'd band bimodality': 0.060955698},
 'HfRu': {
  'half bond': 1.4057466788793478,
  'd band bimodality': 0.035984213},
 'VTi': {
  'half bond': 1.3492900375384898,
  'd band bimodality': 0.073872835},
 'VZr': {
  'half bond': 1.433548576418533,
  'd band bimodality': 0.075774132},
 'VHf': {
  'half bond': 1.4224438084558815,
  'd band bimodality': 0.067249376},
 'VV': {
  'half bond': 1.2957121653111254,
  'd band bimodality': 0.055264365},
 'VNb': {
  'half bond': 1.3686375049626804,
  'd band bimodality': 0.057628941},
 'VTa': {
  'half bond': 1.3717853367417974,
  'd band bimodality': 0.066068535},
 'VMo': {
  'half bond': 1.3306740043626963,
  'd band bimodality': 0.045613084},
 'VW': {
  'half bond': 1.335012267057971,
  'd band bimodality': 0.051287105},
 'VRe': {
  'half bond': 1.314293730973845,
  'd band bimodality': 0.040129116},
 'VRu': {
  'half bond': 1.3035976183363485,
  'd band bimodality': 0.053716135},
 'NbTi': {
  'half bond': 1.4124820911065668,
  'd band bimodality': 0.055754321},
 'NbZr': {
  'half bond': 1.4882610287873488,
  'd band bimodality': 0.068865796},
 'NbHf': {
  'half bond': 1.4786220901348968,
  'd band bimodality': 0.064527259},
 'NbV': {
  'half bond': 1.3686375049626804,
  'd band bimodality': 0.060997487},
 'NbNb': {
  'half bond': 1.4309427850722536,
  'd band bimodality': 0.045007731},
 'NbTa': {
  'half bond': 1.4345465251218361,
  'd band bimodality': 0.059653242},
 'NbMo': {
  'half bond': 1.398669240126693,
  'd band bimodality': 0.062297973},
 'NbW': {
  'half bond': 1.4027128563383746,
  'd band bimodality': 0.063054872},
 'NbRe': {
  'half bond': 1.385380534199102,
  'd band bimodality': 0.06441349},
 'NbRu': {
  'half bond': 1.375355149321527,
  'd band bimodality': 0.050031559},
 'TaTi': {
  'half bond': 1.4163657985472158,
  'd band bimodality': 0.047670376},
 'TaZr': {
  'half bond': 1.492051456329931,
  'd band bimodality': 0.061193684},
 'TaHf': {
  'half bond': 1.482545774915564,
  'd band bimodality': 0.052508696},
 'TaV': {
  'half bond': 1.3717853367417974,
  'd band bimodality': 0.06109191},
 'TaNb': {
  'half bond': 1.4345465251218361,
  'd band bimodality': 0.058327647},
 'TaTa': {
  'half bond': 1.43713094455238,
  'd band bimodality': 0.055337713},
 'TaMo': {
  'half bond': 1.4002653652475745,
  'd band bimodality': 0.067422414},
 'TaW': {
  'half bond': 1.4052758367119946,
  'd band bimodality': 0.067386235},
 'TaRe': {
  'half bond': 1.3870047915533525,
  'd band bimodality': 0.072077729},
 'TaRu': {
  'half bond': 1.376661070232846,
  'd band bimodality': 0.051252415},
 'MoTi': {
  'half bond': 1.371065747735163,
  'd band bimodality': 0.044434511},
 'MoZr': {
  'half bond': 1.45111928111061,
  'd band bimodality': 0.056130108},
 'MoHf': {
  'half bond': 1.439676927855975,
  'd band bimodality': 0.047815038},
 'MoV': {
  'half bond': 1.3306740043626963,
  'd band bimodality': 0.0414007226},
 'MoNb': {
  'half bond': 1.398669240126693,
  'd band bimodality': 0.054996918},
 'MoTa': {
  'half bond': 1.4002653652475745,
  'd band bimodality': 0.049919156},
 'MoMo': {
  'half bond': 1.3719522222459075,
  'd band bimodality': 0.048528345},
 'MoW': {
  'half bond': 1.3762494533691538,
  'd band bimodality': 0.05187558},
 'MoRe': {
  'half bond': 1.3593302287537128,
  'd band bimodality': 0.058396969},
 'MoRu': {
  'half bond': 1.350708486702107,
  'd band bimodality': 0.05558709},
 'WTi': {
  'half bond': 1.376170979651201,
  'd band bimodality': 0.044090028},
 'WZr': {
  'half bond': 1.4560409142592914,
  'd band bimodality': 0.05833828},
 'WHf': {
  'half bond': 1.4440507258597126,
  'd band bimodality': 0.049813273},
 'WV': {
  'half bond': 1.335012267057971,
  'd band bimodality': 0.045131922},
 'WNb': {
  'half bond': 1.4027128563383746,
  'd band bimodality': 0.057126596},
 'WTa': {
  'half bond': 1.4052758367119946,
  'd band bimodality': 0.051456024},
 'WMo': {
  'half bond': 1.3762494533691538,
  'd band bimodality': 0.053686721},
 'WW': {
  'half bond': 1.381285568970158,
  'd band bimodality': 0.055160899},
 'WRe': {
  'half bond': 1.3638891061178575,
  'd band bimodality': 0.064579363},
 'WRu': {
  'half bond': 1.3546825131375058,
  'd band bimodality': 0.059146442},
 'ReTi': {
  'half bond': 1.349085709741297,
  'd band bimodality': 0.042272397},
 'ReZr': {
  'half bond': 1.4316089436393356,
  'd band bimodality': 0.052670758},
 'ReHf': {
  'half bond': 1.4187570251826924,
  'd band bimodality': 0.044649512},
 'ReV': {
  'half bond': 1.314293730973845,
  'd band bimodality': 0.040094164},
 'ReNb': {
  'half bond': 1.385380534199102,
  'd band bimodality': 0.053563412},
 'ReTa': {
  'half bond': 1.3870047915533525,
  'd band bimodality': 0.048732886},
 'ReMo': {
  'half bond': 1.3593302287537128,
  'd band bimodality': 0.047191493},
 'ReW': {
  'half bond': 1.3638891061178575,
  'd band bimodality': 0.050563191},
 'ReRe': {
  'half bond': 1.3472976561516887,
  'd band bimodality': 0.05395104},
 'ReRu': {
  'half bond': 1.3379557710172822,
  'd band bimodality': 0.059565655},
 'RuTi': {
  'half bond': 1.3355601021700063,
  'd band bimodality': 0.032741125},
 'RuZr': {
  'half bond': 1.4209513274152474,
  'd band bimodality': 0.043423636},
 'RuHf': {
  'half bond': 1.4057466788793478,
  'd band bimodality': 0.034896338},
 'RuV': {
  'half bond': 1.3035976183363485,
  'd band bimodality': 0.034108693},
 'RuNb': {
  'half bond': 1.375355149321527,
  'd band bimodality': 0.046415707},
 'RuTa': {
  'half bond': 1.376661070232846,
  'd band bimodality': 0.041416941},
 'RuMo': {
  'half bond': 1.350708486702107,
  'd band bimodality': 0.042539094},
 'RuW': {
  'half bond': 1.3546825131375058,
  'd band bimodality': 0.04624741},
 'RuRe': {
  'half bond': 1.3379557710172822,
  'd band bimodality': 0.048785533},
 'RuRu': {
  'half bond': 1.3273739932864639,
  'd band bimodality': 0.044710103}}

def get_feature(feat, pairs):
    
    avg = 0
    for pair in pairs:
        concentration = pairs[pair]
        avg += B2_properties[pair][feat] * concentration
        
    return avg

def get_feature_SD(feat, pairs):
    
    avg = get_feature(feat,pairs)
    outcomes = []
    proportions = []
    for pair in pairs:
        concentration = pairs[pair]
        outcome = B2_properties[pair][feat]
        #avg += outcome * concentration
        proportions.append(concentration)
        outcomes.append(outcome)
    
    variance = 0
    for x,p in zip(outcomes,proportions):
        variance += (x - avg)**2 * p
    variance = np.sum((np.array(outcomes)-avg)**2 * np.array(proportions))
    SD = variance**.5
    
    return SD

def get_VEC(elements):

    avg = 0
    for element in elements:
        concentration = elements[element]
        avg += element_properties[element]["VEC"] * concentration
        
    return avg
    
def get_VEC_SD(elements):

    avg = 5.7
    outcomes = []
    proportions = []
    for element in elements:
        concentration = elements[element]
        outcome = element_properties[element]["VEC"]
        proportions.append(concentration)
        outcomes.append(outcome)
        
    variance = 0
    for x,p in zip(outcomes,proportions):
        variance += (x - avg)**2 * p
    SD = variance**.5
    
    return SD

def get_RMSAD(chemform):
   
    comp = pg.Composition(chemform)
    elements = {}
    for element in comp:
        elements[str(element)] = comp.get_atomic_fraction(element)
    pairs = {}
    for element1 in elements:
        for element2 in elements:
            pair = element1 + element2
            concentration = elements[element1] * elements[element2]
            pairs[pair] = concentration
          
    #get raw physical features needed for model
    Bond_SD = get_feature_SD("half bond", pairs)
    VEC =  get_VEC(elements) - 5.7
    VEC2 = VEC**2
    VEC_SD = get_VEC_SD(elements)
    VEC_SD2 = VEC_SD**2
    Dip = get_feature("d band bimodality", pairs)
    Dip2 = Dip**2
    
    intercept = 0
    
    RMSAD = intercept
    
    RMSAD += (1.28228602 * (
        Bond_SD
    ))
    
    RMSAD += (20.25233963 * (
        Dip2 * VEC2
    ))
    
    RMSAD += (9.42120305 * (
        Dip2 * VEC_SD2
    ))
    
    return RMSAD

def main():
    chemform = sys.argv[1]
    RMSAD = get_RMSAD(chemform)
    print(RMSAD)
    

if __name__ == "__main__":
    main()
