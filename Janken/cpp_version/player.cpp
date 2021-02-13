#include "Player.h"

Player::Player(string name): name(name), value(0)
{
    // メンバイニシャライザでメンバを初期化
}

string Player::get_name()
{
    return name;
}

int Player::get_value()
{
    return value;
}

void Player::save_history_array(const char* file_name)
{
    ofstream fout(file_name);
    fout << "-1" << endl;
    for(int i = 0; i < history_array.size(); i++)
        fout << history_array[i] << endl;
    fout.close();
}

HumanPlayer::HumanPlayer(string name): Player(name)
{
    // 親クラスのコンストラクタも活用
}

void HumanPlayer::set_value()
{
    value = 0;
    history_array.push_back(value); // 出した手を保存
}

void HumanPlayer::set_value(const char* msg, int start, int end)
{
    double input_num;

    while (1) {
        cout << msg;
        cin >> input_num;
        value = (int)input_num;
        // cout << "value: " << value << endl; // エラー処理確認用

        // 入力された値のエラー処理
        if (!cin.fail() && value >= start && value <= end) {   // 値が数値かつ0～2のとき
            break;
        }
        else {
            cout << "入力エラー！\n0～2の整数値を入力してください。" << endl;
            cin.clear();    // cinのエラー状態を正常(good)に戻す
            cin.ignore(1024, '\n'); // 入力ストリームに残っている可能性のある値を削除する
                                    // 大きめ(1024byte)に読み込んで、改行コードが来るまで削除
        }
    }

    history_array.push_back(value); // 出した手を保存
}

CPUPlayer::CPUPlayer(string name, int start, int end): mt(random_seed()), CPU_value(start, end), Player(name)
{
    // CPU_value(start, end): startからendまでの乱数を生成するインスタンスの生成
    // 親クラスのコンストラクタも活用
}

void CPUPlayer::set_value()
{
    
}

void CPUPlayer::get_cpu_hand_record(string& cpu_hand_record)
{
    vector<int> record = { 0, 0, 0 };
    for (int i = 0; i < history_array.size(); i++) {
        if (history_array[i] == 0)
            record[0]++;
        else if (history_array[i] == 1)
            record[1]++;
        else
            record[2]++;
    }
    cpu_hand_record = "グー(" + to_string(record[0]) + "回), チョキ(" + to_string(record[1]) + "回), パー(" + to_string(record[2]) + "回)";
}
