// Online C++ compiler to run C++ program online
#include<iostream>
#include <cstring>
using namespace std;
 
void Sort(char s1[],char s2[],int n){
    char temp;
    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            if (s1[i] > s1[j]) {
                temp  = s1[i];
                s1[i] = s1[j];
                s1[j] = temp;
            }
            if (s2[i] > s2[j]) {
                temp  = s2[i];
                s2[i] = s2[j];
                s2[j] = temp;
            }
        }
    }
}

int main()
{
    char s1[50], s2[50];
    cout << "str1 : ";
    cin >> s1;
    cout << "str2 : ";
    cin >> s2;
    int n = strlen(s1);
    int n1 = strlen(s2);
    Sort(s1,s2,n);
    cout<<"After sort : "<<endl;
    cout<<s1<<endl;
    cout<<s2<<endl;
    
    for(int i = 0; i<n; i++) {
      if(s1[i] != s2[i]) {    
         printf("not anagrams! \n", s1, s2);
         return 0;
      }
   }
   printf("anagrams! \n");
   return 0;
   }