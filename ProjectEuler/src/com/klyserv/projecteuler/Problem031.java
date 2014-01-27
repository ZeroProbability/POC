package com.klyserv.projecteuler;

public class Problem031 {
	
	public static void main(String[] args) {
		int counter=0;
		for(int coin200p=0;coin200p<=1;coin200p++) {
			int valueSoFar=coin200p*200;
			for(int coin100p=0;coin100p<=2;coin100p++) {
				valueSoFar=coin200p*200+coin100p*100;
				if(valueSoFar>200) {valueSoFar=0;break;}
				for(int coin50p=0;coin50p<=4;coin50p++) {
					valueSoFar=coin200p*200+coin100p*100+coin50p*50;
					if(valueSoFar>200) {valueSoFar=0;break;}
					for(int coin20p=0;coin20p<=10;coin20p++) {
						valueSoFar=coin200p*200+coin100p*100+coin50p*50+coin20p*20;
						if(valueSoFar>200) {valueSoFar=0;break;}
						for(int coin10p=0;coin10p<=20;coin10p++) {
							valueSoFar=coin200p*200+coin100p*100+coin50p*50+coin20p*20+coin10p*10;
							if(valueSoFar>200) {valueSoFar=0;break;}
							for(int coin5p=0;coin5p<=40;coin5p++) {
								valueSoFar=coin200p*200+coin100p*100+coin50p*50+coin20p*20+coin10p*10+coin5p*5;
								if(valueSoFar>200) {valueSoFar=0;break;}
								for(int coin2p=0;coin2p<=100;coin2p++) {
									valueSoFar=coin200p*200+coin100p*100+coin50p*50+coin20p*20+coin10p*10+coin5p*5+coin2p*2;
									if(valueSoFar>200) {valueSoFar=0;break;}
									for(int coin1p=0;coin1p<=200;coin1p++) {
										valueSoFar=coin200p*200+coin100p*100+coin50p*50+coin20p*20+coin10p*10+coin5p*5+coin2p*2+coin1p;
										if(valueSoFar==200) {
											System.out.println(coin200p+"x200 "+coin100p+"x100 "+coin50p+"x50 "+coin20p+"x20 "+coin10p+"x10 "+coin5p+"x5 "+coin2p+"x2 "+coin1p);
											valueSoFar=0;
											counter++;
											break;
										}
									}
								}
							}
						}
					}
				}
			}
		}
		System.out.println("count="+counter);
		
	}

}
