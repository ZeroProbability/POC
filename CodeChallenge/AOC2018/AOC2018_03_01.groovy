import groovy.transform.Canonical

int maxLen = 1200

fullCloth = (0..maxLen).collect { (0..maxLen).collect{0} } as int[][]

def fillEntry(String str) {
   def str1 = str.substring(1)
   def (claim, rest) = str1.split('@').collect{ it.trim() }
   def (sxy, xylen) =  rest.split(':').collect{ it.trim() }
   def (startx, starty) = sxy.split(',').collect{ it.trim().toInteger() }
   def (xlen, ylen) = xylen.split('x').collect{ it.trim().toInteger() }

   
   (startx..(startx + xlen - 1)).each { x -> 
      (starty..(starty + ylen - 1)).each { y -> 
          fullCloth[x][y] += 1
      }
   }
}

def findEntry(String str) {
   def str1 = str.substring(1)
   def (claim, rest) = str1.split('@').collect{ it.trim() }
   def (sxy, xylen) =  rest.split(':').collect{ it.trim() }
   def (startx, starty) = sxy.split(',').collect{ it.trim().toInteger() }
   def (xlen, ylen) = xylen.split('x').collect{ it.trim().toInteger() }

   def unique = (startx..(startx + xlen - 1)).every { x -> 
      (starty..(starty + ylen - 1)).every { y -> 
          fullCloth[x][y] == 1
      }
   }
   if(unique) println claim
}

def entries = new File('./prob3_input.txt').readLines()

entries.each { e -> fillEntry(e) }

println fullCloth.collect { r -> r.findAll{ it > 1 }.size() }.sum()

entries.each { e -> findEntry(e) }

println "-- ended --"
