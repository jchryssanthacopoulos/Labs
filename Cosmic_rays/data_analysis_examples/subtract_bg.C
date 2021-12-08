#include "gethisto.C"

void subtract_bg(const char *file_na,const char *file_bg) {

	// canvas
	TCanvas *c0 = new TCanvas("c0");

	TH1D *h_na = getHistoWithFilter(file_na,514,0,16384,2000);
	TH1D *h_bg = getHistoWithFilter(file_bg,514,0,16384,2000);
	TH1D *h_subtr = (TH1D*)h_na->Clone();
	h_subtr->Add(h_bg,-1);

	h_na->Draw();
	h_subtr->SetLineColor(2);
	h_subtr->Draw("SAME");
	c0->Print("subtr_bg.png");

}

