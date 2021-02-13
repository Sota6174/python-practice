#include "Gnuplot.h"

Gnuplot::Gnuplot()
{
	// gnuplotの起動コマンド
	if ((gnuplot = _popen("gnuplot -persist", "w")) == NULL) {
		cout << "ファイルが見つかりません" << endl;
		exit(1);
	}
}

Gnuplot::~Gnuplot()
{
	// gnuplotの終了
	fprintf(gnuplot, "exit\n");
	_pclose(gnuplot);
}

void Gnuplot::SetTerm(const char* term, int num)
{
	// グラフを出力するターミナルとグラフの番号を指定する
	fprintf(gnuplot, "set term %s %d\n", term, num);
}

void Gnuplot::SetTitle(const char* title)
{
	// グラフのタイトルを設定する
	fprintf(gnuplot, "set title '%s'\n", title);

}

void Gnuplot::SetXLabel(const char* label)
{
	// x軸のラベルを指定する
	fprintf(gnuplot, "set xlabel '%s'\n", label);
}

void Gnuplot::SetYLabel(const char* label)
{
	// y軸のラベルを指定する
	fprintf(gnuplot, "set ylabel '%s'\n", label);
}

void Gnuplot::SetXRange(int lower, int higher)
{
	// x軸の範囲を指定する
	fprintf(gnuplot, "set xrange [%d:%d]\n", lower, higher);
}

void Gnuplot::SetYRange(int lower, int higher)
{
	// y軸の範囲を指定する
	fprintf(gnuplot, "set yrange [%d:%d]\n", lower, higher);
}

void Gnuplot::SetXTics(int start, int step, int end)
{
	// x軸のメモリの表示の仕方を指定する
	fprintf(gnuplot, "set xtics %d, %d, %d\n", start, step, end);
}

void Gnuplot::SetXTics(const char* tics)
{
	// x軸のメモリの表示を任意の文字に変換する
	fprintf(gnuplot, "set xtics(%s)\n", tics);
}

void Gnuplot::SetYTics(const char* tics)
{
	// y軸のメモリの表示を任意の文字に変換する
	fprintf(gnuplot, "set ytics(%s)\n", tics);
}

void Gnuplot::Pause(float pause)
{
	// アニメーションで停止する時間を指定する
	fprintf(gnuplot, "pause %f\n", pause);
}

void Gnuplot::SetAnimation(int flame_num, float pause)
{
	// アニメーションで表示するコマンドの始まり(表示するコマ数を指定する)
	fprintf(gnuplot, "do for[i = 1:%d] {\n", flame_num);
	Pause(pause);
}

void Gnuplot::PlotAnimation(const char* file_name, const char* style, const char* title)
{
	// アニメーションで表示するデータとその表示形式、凡例のタイトルを指定する
	fprintf(gnuplot, "plot \"%s\" every ::0::i %s %s\n", file_name, style, title);
	fflush(gnuplot);
}

void Gnuplot::AddAnimation(const char* file_name, const char* style, const char* title)
{
	// アニメーションで追加で表示するデータとその表示形式、凡例のタイトルを指定する
	fprintf(gnuplot, "replot \"%s\" every ::0::i %s %s\n", file_name, style, title);
	fflush(gnuplot);
}

void Gnuplot::EndAnimation()
{
	// アニメーションで表示するコマンドの終わり
	fprintf(gnuplot, "}\n");
}

void Gnuplot::Reset()
{
	// グラフに関する設定を削除する
	fprintf(gnuplot, "reset\n");
}

void Gnuplot::SetHistogramStyle(double width)
{
	// ヒストグラムの1つ1つの棒の幅を指定する(min 0.0, max 1.0)
	fprintf(gnuplot, "set boxwidth %f relative\n", width);
	fprintf(gnuplot, "set style fill solid border -1\n");
}

void Gnuplot::PlotHistogram(const char* file_name, const char* style, const char* title)
{
	// データとその表示形式、凡例のタイトルを指定してヒストグラムを表示する
	fprintf(gnuplot, "plot \"%s\" %s %s\n", file_name, style, title);
	fflush(gnuplot);
}

void Gnuplot::Plot(const char* file_name, const char* style, const char* title)
{
	// データとその表示形式、凡例のタイトルを指定して折れ線グラフを表示する
	fprintf(gnuplot, "plot \"%s\" %s %s\n", file_name, style, title);
	fflush(gnuplot);
}
