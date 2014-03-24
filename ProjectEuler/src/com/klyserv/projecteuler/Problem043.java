package com.klyserv.projecteuler;

import java.util.Arrays;
import java.util.List;

public class Problem043 {
	
	public static void main(String[] args) {
		final long[] count={0};
		Permutation.compute(Arrays.asList(0,1,2,3,4,5,6,7,8,9), new PermutationListener() {
			
			@Override
			public void listen(List<Object> occur) {
				int d2d3d4=(int)occur.get(1)*100+(int)occur.get(2)*10+(int)occur.get(3);
				if(d2d3d4%2!=0) return;
				int d3d4d5=(int)occur.get(2)*100+(int)occur.get(3)*10+(int)occur.get(4);
				if(d3d4d5%3!=0) return;
				int d4d5d6=(int)occur.get(3)*100+(int)occur.get(4)*10+(int)occur.get(5);
				if(d4d5d6%5!=0) return;
				int d5d6d7=(int)occur.get(4)*100+(int)occur.get(5)*10+(int)occur.get(6);
				if(d5d6d7%7!=0) return;
				int d6d7d8=(int)occur.get(5)*100+(int)occur.get(6)*10+(int)occur.get(7);
				if(d6d7d8%11!=0) return;
				int d7d8d9=(int)occur.get(6)*100+(int)occur.get(7)*10+(int)occur.get(8);
				if(d7d8d9%13!=0) return;
				int d8d9d10=(int)occur.get(7)*100+(int)occur.get(8)*10+(int)occur.get(9);
				if(d8d9d10%17!=0) return;
				//System.out.println(Helper.toLong(occur));
				count[0]+=Helper.toLong(occur);
			}
		});
		System.out.println(count[0]);
	}

}
