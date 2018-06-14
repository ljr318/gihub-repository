<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<div align="center">
		<%
			
		String str = request.getParameter("number");
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
 	
        
	
		out.print("["+sb.toString()+"]" );
			
		%>
		<a href="index.jsp">返回</a>
	</div>
</body>
</html>