package com.klyserv.projecteuler;

import java.util.HashMap;
import java.util.Map;

public class Combination {
	
	private CombinationListener cl;
	
	private void processOneElement(Map<Object,Integer> fullMap, Map<Object,Integer> chooseMap){
		if(fullMap.size()==0) {
			cl.listen(chooseMap);
			return;
		}
		Object key=fullMap.keySet().iterator().next();
		int count=fullMap.remove(key);
		for(int i=0;i<=count;i++) {
			chooseMap.put(key, i);
			processOneElement(fullMap, chooseMap);
		}
		fullMap.put(key, count);
	}
	
	public Combination(Map<Object,Integer> map, CombinationListener cl) {
		this.cl=cl;
		processOneElement(new HashMap<Object, Integer>(map), new HashMap<Object, Integer>());
	}
	
	public static void main(String[] args) {
		Map<Object,Integer> map=new HashMap<Object, Integer>();
		map.put(1, 1);
		map.put(2, 1);
		map.put(3, 2);
		
		new Combination(map, new CombinationListener() {
			
			@Override
			public void listen(Map<Object, Integer> occur) {
				for(Object key:occur.keySet()) {
					System.out.print(key+"x"+occur.get(key)+" ");
				}
				System.out.println();
				
			}
		});
	}

}
