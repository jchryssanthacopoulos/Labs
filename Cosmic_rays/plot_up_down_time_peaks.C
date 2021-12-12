/*
    This macro plots the time calibration for the peaks for the UP and DOWN detectors

    To run it, first run:
        .L data_analysis_examples/gethisto.C
*/


void plot_up_time_peaks() {
   TH1D *hist = getHistoWithFilterFromChannelWithCalibration(
      "files/overnight_after_fix_coinc_remapping.root", "", 200, 0, 30, 1, 3, 5000, 10000,
      0.0012296920435007485, 1.3806172257509797
   );

   TF1 *g1 = new TF1("g1", "gaus+pol1(3)", 7, 15);
   TF1 *g2 = new TF1("g2", "gaus+pol1(3)", 18, 25);

   Double_t par1[5] = {42, 11, 1.4, 0, 0};
   Double_t par2[5] = {37, 22, 1.6, 0, 0};

   g1->SetParameters(par1);
   g2->SetParameters(par2);

   hist->Fit(g1, "R");
   hist->Fit(g2, "R+");

   auto c1 = new TCanvas("c1","c1",0,0,1000,700);
   c1->SetGrid();
   gStyle->SetPadLeftMargin(0.15);

   hist->SetLineColor(4);
   hist->SetLineWidth(2);
   hist->SetStats(0);
   hist->Draw();

   hist->SetTitle("");
   hist->GetXaxis()->SetTitle("Time (ns)");
   hist->GetYaxis()->SetTitle("Count");
   hist->GetXaxis()->CenterTitle();
   hist->GetYaxis()->CenterTitle();
   hist->GetXaxis()->SetLabelSize(0.05);
   hist->GetYaxis()->SetLabelSize(0.05);
   hist->GetXaxis()->SetTitleSize(0.05);
   hist->GetYaxis()->SetTitleSize(0.05);
}



void plot_down_time_peaks() {
   TH1D *hist = getHistoWithFilterFromChannelWithCalibration(
      "files/overnight_after_fix_coinc_remapping.root", "", 200, 0, 30, 2, 3, 5000, 10000,
      0.0012366149543127432, -3.790202684122164
   );

   TF1 *g1 = new TF1("g1", "gaus+pol1(3)", 7, 15);
   TF1 *g2 = new TF1("g2", "gaus+pol1(3)", 18, 25);

   Double_t par1[5] = {42, 11, 1.4, 0, 0};
   Double_t par2[5] = {37, 22, 1.6, 0, 0};

   g1->SetParameters(par1);
   g2->SetParameters(par2);

   hist->Fit(g1, "R");
   hist->Fit(g2, "R+");

   auto c1 = new TCanvas("c1","c1",0,0,1000,700);
   c1->SetGrid();
   gStyle->SetPadLeftMargin(0.15);

   hist->SetLineColor(4);
   hist->SetLineWidth(2);
   hist->SetStats(0);
   hist->Draw();

   hist->SetTitle("");
   hist->GetXaxis()->SetTitle("Time (ns)");
   hist->GetYaxis()->SetTitle("Count");
   hist->GetXaxis()->CenterTitle();
   hist->GetYaxis()->CenterTitle();
   hist->GetXaxis()->SetLabelSize(0.05);
   hist->GetYaxis()->SetLabelSize(0.05);
   hist->GetXaxis()->SetTitleSize(0.05);
   hist->GetYaxis()->SetTitleSize(0.05);
}
