// Playerクラス: ゲーム参加者それぞれの情報を定義・操作するクラス
//               デストラクタはreturn, delete時にデフォルトデストラクタが呼び出される
// HumanPlayerクラス: Playerクラスを仮想継承した人間のゲーム参加者用のクラス
// CPUPlayerクラス: Playerクラスを仮想継承したコンピュータ用のクラス

#pragma once
#include <iostream>
#include <string>
#include <random>
#include <vector>
#include <fstream>
using namespace std;

class Player
{
    string name;
protected:  // 継承先のクラスからも呼び出せる
    int value;
    vector<int> history_array;   // 変数を格納する可変長の配列
public:
    Player(string name); // コンストラクタ
    virtual void set_value() = 0;   // 純粋仮想関数(継承先で必ず実装しなければならない)
    string get_name();
    int get_value();
    void save_history_array(const char* file_name);
};

// Playerクラスを仮想継承
class HumanPlayer: public virtual Player
{
public:
    HumanPlayer(string name);
    void set_value() override;
    void set_value(const char* msg, int start, int end);
};

// Playerクラスを仮想継承
class CPUPlayer: public virtual Player
{
    random_device random_seed;  // 非決定的な乱数生成器(疑似乱数の初期シード)
    mt19937_64 mt;   // 乱数生成エンジン
    uniform_int_distribution<int> CPU_value; // 整数の一様分布乱数を生成するクラスのインスタンス
public:
    CPUPlayer(string name, int start, int end);
    void set_value() override;
    void get_cpu_hand_record(string& cpu_hand_record);
};
