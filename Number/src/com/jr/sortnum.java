package com.jr;

import java.util.Scanner;

public class sortnum {
	public static void main(String[] args) {
        
       Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
 
        String[] strs = str.split(",");// 分割
        int[] is = new int[strs.length];
        for (int i = 0; i < strs.length; i++) {// 遍历String数组，赋值给int数组
            is[i] = Integer.parseInt(strs[i]);
        }
 
int temp = 0;
		
		for(int i = 0;i < is.length;i++)
		{
			for(int j = 0;j < is.length-i-1;j++)
			{
				if(is[j] == 0)
				{
					temp = is[j+1];
					is[j+1]=is[j];
					is[j] = temp;
				}
				else if(is[j+1] == 0)
				{
					is[j+1]=0;
					
				}
				else if(is[j]>=is[j+1])
				{
					temp = is[j];
					is[j] = is[j+1];
					is[j+1] = temp;
				}	
					
			}}
 
        StringBuffer sb = new StringBuffer();
        for (int i1 = 0; i1 < is.length; i1++) {// 遍历进行拼接
            if (i1 == is.length - 1) {
                sb.append(is[i1]);
            } else {
                sb.append(is[i1] + ",");
            }
        }
 
        System.out.println(sb.toString());
	}
}
