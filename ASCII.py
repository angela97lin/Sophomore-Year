﻿#Angela Lin
#pd 06
#HW 13
#03/11/13

##
##1. replace(s,q,r) takes 3 string inputs and replaces any occurrences of q in s with r. If there is no occurrence of q in s, then s is returned unchanged.
##e.g.,
##replace(“Winter is coming”, “Winter”, “Spring”) → “Spring is coming”
##replace(“Mice run this planet”, “mice”, “dolphins”) → “Mice run this planet”

def replace(s,q,r):
    if s.find(q)!=-1: #check if q is in s
      return s[0:s.find(q)]+r+s[(s.find(q)+len(q)):] #if q is in s, then it will return all characters from 0 to q, then adds r to the string, then add all the characters after q to the end of the original s.
    else:
        return s #otherwise, the original string, s, is returned
    
        

print replace("Winter is coming", "Winter","Spring")
print "should be..."
print "Spring is coming"

print replace("Mice run this planet", "mice","dolphins")
print "should be..."
print "Mice run this planet"


print replace("Starbucks is amazing", "amazing","expensive")
print "should be..."
print "Starbucks is expensive"


##2. tablefyASCII() returns a string of valid HTML code generating a 2-column, 53-row table. This table will show the letters
#of the alphabet and their associated ASCII value. Letters on the left, numbers on the right.


def tablefyASCII():
    upperCase=65
    lowerCase=97
    tfy=""
    tfy+="<table border=1><tr><td>Letters</td><td>ASCII Value/Number</td></tr>" #Code used to set up a table in HTML with a border of 1
    while upperCase<91: #takes care of uppercase letters, as ord() of any uppercase letter is between 65 and 90, inclusive.
        tfy+="<tr><td>"+str(chr(upperCase))+"</td><td>"+str(upperCase)+"</td></tr>"
        upperCase+=1 
    while lowerCase<123:
        tfy+="<tr><td>"+str(chr(lowerCase))+"</td><td>"+str(lowerCase)+"</td></tr>"#the ord() of lowercase letters are between 97 and 122, inclusive.
        lowerCase+=1
    tfy+="</table>"
    return tfy


print tablefyASCII()
print "should be..."
print "<table border=1><tr><td>Letters</td><td>ASCII Value/Number</td></tr><tr><td>A</td><td>65</td></tr><tr><td>B</td><td>66</td></tr><tr><td>C</td><td>67</td></tr><tr><td>D</td><td>68</td></tr><tr><td>E</td><td>69</td></tr><tr><td>F</td><td>70</td></tr><tr><td>G</td><td>71</td></tr><tr><td>H</td><td>72</td></tr><tr><td>I</td><td>73</td></tr><tr><td>J</td><td>74</td></tr><tr><td>K</td><td>75</td></tr><tr><td>L</td><td>76</td></tr><tr><td>M</td><td>77</td></tr><tr><td>N</td><td>78</td></tr><tr><td>O</td><td>79</td></tr><tr><td>P</td><td>80</td></tr><tr><td>Q</td><td>81</td></tr><tr><td>R</td><td>82</td></tr><tr><td>S</td><td>83</td></tr><tr><td>T</td><td>84</td></tr><tr><td>U</td><td>85</td></tr><tr><td>V</td><td>86</td></tr><tr><td>W</td><td>87</td></tr><tr><td>X</td><td>88</td></tr><tr><td>Y</td><td>89</td></tr><tr><td>Z</td><td>90</td></tr><tr><td>a</td><td>97</td></tr><tr><td>b</td><td>98</td></tr><tr><td>c</td><td>99</td></tr><tr><td>d</td><td>100</td></tr><tr><td>e</td><td>101</td></tr><tr><td>f</td><td>102</td></tr><tr><td>g</td><td>103</td></tr><tr><td>h</td><td>104</td></tr><tr><td>i</td><td>105</td></tr><tr><td>j</td><td>106</td></tr><tr><td>k</td><td>107</td></tr><tr><td>l</td><td>108</td></tr><tr><td>m</td><td>109</td></tr><tr><td>n</td><td>110</td></tr><tr><td>o</td><td>111</td></tr><tr><td>p</td><td>112</td></tr><tr><td>q</td><td>113</td></tr><tr><td>r</td><td>114</td></tr><tr><td>s</td><td>115</td></tr><tr><td>t</td><td>116</td></tr><tr><td>u</td><td>117</td></tr><tr><td>v</td><td>118</td></tr><tr><td>w</td><td>119</td></tr><tr><td>x</td><td>120</td></tr><tr><td>y</td><td>121</td></tr><tr><td>z</td><td>122</td></tr></table>"


