// Gnuplotクラス: Gnuplotでグラフを表示するためのクラス
//                ヒストグラムを表示する機能とアニメーションで折れ線グラフを表示する機能のみ実装

#pragma once
#include <iostream>
#include <stdio.h>
using namespace std;

class Gnuplot {
	FILE* gnuplot;
public:
	Gnuplot();
	~Gnuplot();
	void SetTerm(const char* term, int num);
	void SetTitle(const char* title);
	void SetXLabel(const char* label);
	void SetYLabel(const char* label);
	void SetXRange(int lower, int higher);
	void SetYRange(int lower, int higher);
	void SetXTics(int start, int step, int end);
	void SetXTics(const char* tics);
	void SetYTics(const char* tics);
	void Pause(float pause);
	void SetAnimation(int flame_num, float pause);
	void PlotAnimation(const char* file_name, const char* style, const char* title);
	void AddAnimation(const char* file_name, const char* style, const char* title);
	void EndAnimation();
	void Reset();
	void SetHistogramStyle(double width);
	void PlotHistogram(const char* file_name, const char* style, const char* title);
	void Plot(const char* file_name, const char* style, const char* title);
};
