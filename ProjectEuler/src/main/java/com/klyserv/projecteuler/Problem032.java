package com.klyserv.projecteuler;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Problem032 {
	
	private static int isSolution(List<Object> o, int n1,int n2, int n3){
		String firstNumber="", secondNumber="", thirdNumber="";
		int i=0;
		for(;i<n1;i++)
			firstNumber+=o.get(i);
		for(;i<(n1+n2);i++)
			secondNumber+=o.get(i);
		for(;i<(n1+n2+n3);i++)
			thirdNumber+=o.get(i);
		if(Integer.parseInt(firstNumber)*Integer.parseInt(secondNumber)==Integer.parseInt(thirdNumber)) {
			System.out.println(firstNumber+" x "+secondNumber+" = "+thirdNumber);
			return Integer.parseInt(thirdNumber);
		}
		return 0;
	}

	public static void main(String[] args) {
		final Set<Integer> counter=new HashSet<Integer>();
		Permutation.compute(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9),
				new PermutationListener() {

					@Override
					public void listen(List<Object> occur) {
						for (int firstNumberSize = 1; firstNumberSize < 7; firstNumberSize++) {
							for (int secondNumberSize = 1; secondNumberSize < 7; secondNumberSize++) {
								if(firstNumberSize+secondNumberSize>9) break;
								for (int thirdNumberSize = 1; thirdNumberSize < 7; thirdNumberSize++) {
									if(firstNumberSize+secondNumberSize+thirdNumberSize>9) break;
									if(firstNumberSize+secondNumberSize+thirdNumberSize==9) {
										int thirdNumber=0;
										if((thirdNumber=isSolution(occur, firstNumberSize, secondNumberSize, thirdNumberSize))>0){
											counter.add(thirdNumber);
										}
									}
								}
							}

						}

					}
				});
		
		Integer sum=0;
		for(Integer i:counter)
			sum+=i;
		System.out.println("sum="+sum);
	}

}
