// See https://aka.ms/new-console-template for more information
// int int1 = 0;
// int int2 = 0;

// Console.WriteLine("請輸入第一個整數:");
// int1 = int.Parse(Console.ReadLine());
// Console.WriteLine("請輸入第二個整數:");
// int2 = int.Parse(Console.ReadLine());

// if(int1>int2){
//     Console.WriteLine("{0}>{1}",int1,int2);
// }else if(int1<int2){
//     Console.WriteLine("{0}<{1}",int1,int2);
// }else{
//     Console.WriteLine("{0}={1}",int1,int2);
// }

// int hour = 0;
// Console.WriteLine("請輸入現在時間(小時)");
// hour = int.Parse(Console.ReadLine());

// switch(hour){
//     case 19:
//     case 20:
//         Console.WriteLine("一更");
//         break;
//     case 21:
//     case 22:
//         Console.WriteLine("二更");
//         break;
//     case 23:
//     case 1:
//         Console.WriteLine("三更");
//         break;
//     case 2:
//     case 3:
//         Console.WriteLine("四更");
//         break;
//     case 4:
//     case 5:
//         Console.WriteLine("五更");
//         break;
//     case 6:
//     case 7:
//     case 8:
//     case 9:
//     case 10:
//     case 11:
//     case 12:
//     case 13:
//     case 14:
//     case 15:
//     case 16:
//     case 17:
//     case 18:
//         Console.WriteLine("早上");
//         break;
//     default:
//         Console.WriteLine("輸入錯誤");
//         break;

// }

// int k =1;
// int wt = 0;
// while(k<=100){
//     if(wt==5){
//         Console.WriteLine();
//         wt=0;
//     }
//     if (k%4==0){
//         Console.Write("{0}\t",k);
//         wt++;
//     }
//     k++;
// }

// int num = 0;
// int cp = 0;
// Console.WriteLine("請輸入一個數字");
// num = int.Parse(Console.ReadLine());
// cp = num;
// //階乘
// int ans = 0;

// while(num>0){
//     if(ans==0){
//         ans = num;
//     }else{
//         ans = ans * num;
//     }
//     num--;
// }



// Console.WriteLine("{0}! = {1}",cp,ans);

using System.Text.RegularExpressions;

bool isPrime = false;
do{
    int test = 0;
    string test2 = "";

    Console.WriteLine("請輸入一個數字");
    test2 = Console.ReadLine();
    Regex tt = new Regex("^[0-9]+$");

    if(tt.IsMatch(test2)){
        test = int.Parse(test2);
        Console.WriteLine("輸入的數字為{0}",test);
        isPrime = true;
    }else{
        continue;
    }






}while(!isPrime);