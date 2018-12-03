def distance(String s1, String s2) {
   def s1array = s1.toList()
   def s2array = s2.toList()

   int d = 0
   for(int i: (0..(s1array.size()))) {
      if(s1array[i] != s2array[i]) d++
   }
   return d
}

def file = '/home/anbu/poc/CodeChallenge/AOC2018/prob2_input.txt'

def strings = new File(file).readLines()
//strings = ["abcd" , "abdf", "xyza", "defg"]

println "-"*80
int minDistance = 1000
def minStr1 = ""
def minStr2 = ""
for(def str1i: (0..(strings.size()-2))) {
    for(def str2i: ((str1i+1)..(strings.size()-1))) {
       def newDistance =  distance(strings[str1i], strings[str2i])
       if(newDistance < minDistance) {
          minDistance = newDistance
          minStr1 = strings[str1i]
          minStr2 = strings[str2i]
       }
       // println " => ${strings[str1i]} ${strings[str2i]}"
    }
}

println minDistance
println minStr1
println minStr2
