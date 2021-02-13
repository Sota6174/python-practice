// Jankenクラス: ジャンケンのゲームに関する情報を定義・操作するクラス
//               コンストラクタははインスタンス生成時にデフォルトコンストラクタが呼び出される
//               デストラクタはreturn, delete時にデフォルトデストラクタが呼び出される
//               Playerクラスの性質を引き継がせたいクラスではないため継承するのではなく、
//               includeして機能(メソッド)だけ呼び出して使う

#pragma once
#include "Player.h"
using namespace std;

class Janken
{
    int win = 0;    // Userが勝利した回数
    int lose = 0;   // Userが敗北した回数
    int draw = 0;   // 引き分けた回数
    char hand[3][10] = { "グー", "チョキ", "パー" };  // 手
    int count = 0;  // ジャンケンの回数(手を出した回数)のカウンター

public:
    void instruction();
    void set_user_hand(HumanPlayer &user);
    void set_cpu_hand(CPUPlayer &cpu);
    void judge(HumanPlayer &user, CPUPlayer &cpu);
    int retry();
    void score();                           
    int get_count();
    void get_user_record(string& record);
    void save_user_record(const char* file_name);
};
