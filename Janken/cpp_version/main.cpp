#include "Janken.h"
// #include "Gnuplot.h"
using namespace std;

int main()
{
    const char* user_name = "User1";
    const char* cpu_name = "CPU1";
    int retry = 1;
    int start = 0;
    int end = 2;
    const char* file_name1 = "user_hand.txt";
    const char* file_name2 = "cpu_hand.txt";
    const char* file_name3 = "user_record.txt";
    string file_name4 = "cpu_hand_test0.txt";
    int playtimes = 1;
    string user_record;
    string cpu_hand_record;
    string title = "Userの戦績: ";
    CPUPlayer* cpu_test = 0;
    const int N = 100; 

    // インスタンスの生成・初期化
    Janken janken;
    HumanPlayer user(user_name);
    CPUPlayer cpu(cpu_name, start, end);
    // Gnuplot gp;

    // 遊び方のインストラクション
    janken.instruction();

    // ジャンケンゲームスタート
    do {
        // Userの出す手を入力
        janken.set_user_hand(user);

        // CPUの手を乱数で決定
        janken.set_cpu_hand(cpu);

        // 勝敗を判定・結果を出力
        janken.judge(user, cpu);

        // 再戦するか確認
        retry = janken.retry();
    } while (retry != 0);


    // // USERとCPUの手の推移
    // cout << "\n<手の推移>をGnuplotで出力" << endl;
    // user.save_history_array(file_name1);
    // cpu.save_history_array(file_name2);
    // playtimes = janken.get_count();

    // // Gnuplotでアニメーションを表示
    // gp.SetTerm("qt", 1);
    // gp.SetTitle("手の推移");
    // gp.SetXLabel("ゲーム回数");
    // gp.SetYLabel("出した手");
    // gp.SetXRange(1, playtimes);
    // gp.SetYRange(0, 2);
    // gp.SetXTics(1, 1, playtimes);
    // gp.SetYTics("'グー' 0, 'チョキ' 1, 'パー' 2");
    // gp.SetAnimation(playtimes, 0.5);
	// gp.PlotAnimation(file_name1, "w lp ls 0 pt 1 lc 1 lw 5", "title 'UserHand'");
	// gp.AddAnimation(file_name2, "w lp ls 1 pt 2 lc 3 lw 3", "title 'CPUHand'");
	// gp.EndAnimation();
    // gp.Reset();


    // // USERの勝敗、引き分け数
    // cout << "\n<" << user_name << "の戦績(ヒストグラム)>をGnuplotで出力" << endl;
    // janken.get_user_record(user_record);
    // janken.save_user_record(file_name3);

    // // Gnuplotでヒストグラムを表示
    // gp.SetTerm("qt", 2);
    // gp.SetTitle((title+user_record).c_str());
    // gp.SetYLabel("回数");
    // gp.SetXRange(0, 4);
    // gp.SetYRange(0, playtimes);
    // gp.SetXTics("'勝ち' 1, '負け' 2, '引き分け' 3");
    // gp.SetHistogramStyle(0.8);
    // gp.PlotHistogram(file_name3, "w boxes lc 2 lw 2", "notitle");
    // gp.Reset();


    // // その他のデータの可視化１: ジャンケンゲームの最終結果
    // janken.score();


    // // その他のデータの可視化２: CPUの出す手の不連続・不規則性の確認
    // for (int i = 0; i < 5; i++) {
    //     // cpu_testはポインタのため関数はアロー演算子で呼び出す
    //     cpu_test = new CPUPlayer(cpu_name, start, end);  // インスタンスの生成(動的なメモリ管理)
    //     file_name4.replace(13, 1, to_string(i + 1));

    //     cout << "\n<CPUの手の推移>の確認( " << i+1 << "回目 )" << endl;

    //     // CPUの手を乱数で100回生成
    //     for (int i = 0; i < N; i++)
    //         janken.set_cpu_hand(*cpu_test);

    //     // CPUの手を保存
    //     cpu_test->save_history_array(file_name4.c_str());

    //     // CPUの出したそれぞれの手の回数を取得
    //     cpu_test->get_cpu_hand_record(cpu_hand_record);

    //     // Gnuplotで折れ線グラフを表示
    //     gp.SetTerm("qt", i+3);
    //     title = "CPUの手の推移: ";
    //     cout << "Check" << i+1 << ": " << (title + cpu_hand_record).c_str() << endl;
    //     gp.SetTitle((title + cpu_hand_record).c_str());
    //     gp.SetXLabel("回数");
    //     gp.SetYLabel("出した手");
    //     gp.SetXRange(1, N);
    //     gp.SetYRange(0, 2);
    //     gp.SetXTics(1, 10, N);
    //     gp.SetYTics("'グー' 0, 'チョキ' 1, 'パー' 2");
    //     gp.Plot(file_name4.c_str(), "w lp ls 1 pt 2 lc 3 lw 1", "title 'CPURandHand'");
    //     gp.Reset();

    //     delete cpu_test; // インスタンスの削除(動的なメモリ管理)
    // }

    return 0;
}
