#include "janken.h"

void Janken::instruction()
{
    // ジャンケンのゲームに関する説明を出力する
    cout << "<ジャンケンゲームのインストラクション>\n" << endl;
    cout << "これからCPUとジャンケンしていただきます。" << endl;
    cout << "「Input user_hand: 」の後に0～2の数字を入力してください。" << endl;
    cout << "「グー」-> 0, 「チョキ」-> 1, 「パー」-> 2です。" << endl;
    cout << "ジャンケンの度に終了するか聞かれるので終了する場合は「0」を入力してください。" << endl;
    cout << "「0」以外の数字が入力された場合はゲームが継続されます。" << endl;
    cout << "終了後に結果が表示されます。\n" << endl;
}

void Janken::set_user_hand(HumanPlayer &user)
{
    // userが手を出す(値の保存はPlayerクラスの役割)
    cout << count + 1 << "回目)" << endl;
    cout << "「グー」-> 0, 「チョキ」-> 1, 「パー」-> 2" << endl;
    user.set_value("Input user_hand: ", 0, 2);
}

void Janken::set_cpu_hand(CPUPlayer &cpu)
{
    // cpuが手を出す(値の保存はPlayerクラスの役割)
    cpu.set_value();
}

void Janken::judge(HumanPlayer &user, CPUPlayer &cpu)
{
    // ジャンケンの勝ち負けを判定する
    int user_hand = user.get_value();
    int cpu_hand = cpu.get_value();
    int temp = (user_hand - cpu_hand + 3) % 3;

    cout << "Userの手: " << hand[user_hand] << ", ";
    cout << "CPUの手 : " << hand[cpu_hand] << endl;
    if (temp == 0) {         // 引き分け
        draw++;
        cout << "result: 引き分けです。\n" << endl;
    }
    else if (temp == 1) {    // Userの負け
        lose++;
        cout << "result: あなたの負けです。\n" << endl;
    }
    else {                  // Userの勝ち
        win++;
        cout << "result: あなたの勝ちです。\n" << endl;
    }

    count++;
}

int Janken::retry()
{
    // もう1ゲームやるか確認する
    int retry;

    while (1) {
        cout << "もう一回やりますか？[終了->0, 継続->else_integer]: ";
        cin >> retry;
        // 入力された値のエラー処理
        if (!cin.fail()) {   // 値が整数値のとき
            break;
        }
        else {
            cout << "入力エラー！\n整数値を入力してください。" << endl;
            cin.clear();            // cinのエラー状態を正常(good)に戻す
            cin.ignore(1024, '\n'); // 入力ストリームに残っている可能性のある値を削除する
                                    //      大きめ(1024byte)に読み込んで、改行コードが来るまで削除
        }
    }
    cout << endl;

    return retry;
}

void Janken::score()
{
    // ジャンケンゲームの最終結果を出力する
    cout << "<最終結果>\n" << endl;
    cout << "\t | 勝ち | 負け | 引き分け" << endl;
    cout << "User\t |  " << win << "   |  " << lose << "   |  " << draw << endl;
    cout << "CPU \t |  " << lose << "   |  " << win << "   |  " << draw << endl;
    cout << endl;
}

int Janken::get_count()
{
    return count;
}

void Janken::get_user_record(string& record)
{
    // ゲームに参加したUserの戦績をstringで返す(引数は参照渡し)
    record = to_string(win) + "勝" + to_string(lose) + "敗" + to_string(draw) + "引き分け";
    cout << "record: " << record << endl;
}

void Janken::save_user_record(const char* file_name)
{
    // ファイルのUserの戦績を出力する(0行目の値は調整用)
    ofstream fout(file_name);
    fout << 0 << endl;
    fout << win << endl;
    fout << lose << endl;
    fout << draw << endl;
    fout.close();
}
