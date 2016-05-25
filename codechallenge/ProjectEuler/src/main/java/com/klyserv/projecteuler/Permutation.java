package com.klyserv.projecteuler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.TreeSet;
import java.util.List;

public class Permutation {

	private static void permutationx(TreeSet<Object> fullList, List<Object> displayList, PermutationListener pl){
		if(fullList.isEmpty()) {
			pl.listen(Collections.unmodifiableList(displayList));
		}
		for(Object p0:fullList) {
			TreeSet<Object> fullList1=new TreeSet<Object>(fullList);
			fullList1.remove(p0);
			displayList.add(p0);
			permutationx(fullList1,displayList,pl);
			displayList.remove(p0);
		}
	}
	
	public static void compute(Collection<?> fullList, PermutationListener pl) {
		TreeSet<Object> s=new TreeSet<Object>(fullList);
		permutationx(s, new ArrayList<Object>(), pl);
	}
	
	public static void main(String[] args) {
		compute(Arrays.asList(0,1,2,3,4,5,6), new PermutationListener() {
			
			@Override
			public void listen(List<Object> occur) {
				System.out.println(occur);
				
			}
		});
	}
	
	
}
