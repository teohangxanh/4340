#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

/*
Author: Ted Dang
Date created: 03/15/2020
Usage: Returns gcd of two numbers
*/
int gcd(int n1, int n2){
    int a, b;
    if (n1 >= n2){
        a = n1;
        b = n2;
    }
    else{
        a = n2;
        b = n1;
    }
    while (b > 0){
        int rem = a % b;
        a = b;
        b = rem;
    }
    return a;
}

/*
Author: Ted Dang
Date created: 03/15/2020
Usage: Returns a vector of prime factors of the given number
*/
// string findGCD(vector<int> v){
//     string ans;
//     int my_gcd;
//     if (v.size() == 1){
//         if (v[0] == 1) ans = "YES";
//         else ans = "NO";
//     }
//     else{
//         my_gcd = gcd(v[0], v[1]);
//         if (v.size() == 2){
//             if (my_gcd == 1) ans = "YES";
//             else ans = "NO";
//         }
//         else{
//             for (int i = 2; i < v.size(); i++){
//                 my_gcd = gcd(v[i], my_gcd);
//             }
//             if (my_gcd == 1) ans = "YES";
//             else ans = "NO";
//         }
//     }
//     cout << my_gcd << endl;
//     return ans;
// }

/*
Author: Ted Dang
Date created: 03/15/2020
Usage: Returns true if a number is prime
*/
bool isPrime(long n){
    for (int i = 2; i <= sqrt(n); i++){
        if (n % i == 0) return false;
    }
    return true;
}

/*
Author: Ted Dang
Date created: 03/15/2020
Usage: Returns a vector of prime factors of the given number
*/
vector<int> findPrimeFactor(long n){
    vector<int> v;
    for (int i = 2; i <= sqrt(n); i++){
        if (n % i == 0 && isPrime(i)){
            v.push_back(i);
            while (n % i == 0){
                n /= i;
            }
        }
    }
    if (n != 1) v.push_back(n);
    return v;
}

/*
Author: Ted Dang
Date created: 03/15/2020
Usage: Returns a number representing the highest exponent of a prime factor of number n
*/
struct factor{
    int fact;
    int exp;
};

vector<factor> findHighestExpFact(long n){
    vector<factor> v;
    for (int i = 2; i <= sqrt(n); i++){
        if (n % i == 0 && isPrime(i)){
            factor m;
            m.fact = i;
            m.exp = 1;
            v.push_back(m);
            while (n % i == 0){
                n /= i;
                v[i].exp++;
            }
        }
    }
    if (n != 1) {
        factor m;
        m.fact = i;
        m.exp = 1;
        v.push_back(m, 1);
    }
    return v;
}

/*
Author: Ted Dang
Date created: 03/15/2020
Usage: Print a vector's element
*/
void print(vector<int> v){
    for (int i = 0; i < v.size(); i++){
        cout << v[i] << endl;
    }
}

int main(){
    vector<int> v = findPrimeFactor(500);
    cout << endl;
    print(v);


    return 0;
}
