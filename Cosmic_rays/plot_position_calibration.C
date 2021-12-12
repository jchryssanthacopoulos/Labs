/*
    This macro plots the position calibration for the peaks and overall
    for the UP and DOWN detectors

    To run it, first run:
        .L data_analysis_examples/gethisto.C
*/


void plot_position_calibration() {
    TH1D *hist_up = getHistoForChannelFromTreeWithCalibration(
        "files/overnight_after_fix_coinc_remapping.root", 1, 400, 0, 1.5, 0.00010914992943457062, -0.7429201535521206
    );
    TH1D *hist_down = getHistoForChannelFromTreeWithCalibration(
        "files/overnight_after_fix_coinc_remapping.root", 2, 400, 0, 1.5, 0.0001066245854969239, -1.1976638553317625
    );

    hist_up->SetStats(0);
    hist_down->SetStats(0);

    hist_up->SetLineColor(4);
    hist_down->SetLineColor(2);

    auto c1 = new TCanvas("c1","c1",0,0,700,600);
    c1->SetGrid();
    gStyle->SetPadLeftMargin(0.15);

    hist_up->Draw();
    hist_down->Draw("same");

    hist_up->SetLineWidth(2);
    hist_down->SetLineWidth(2);

    hist_up->SetTitle("");
    hist_up->GetXaxis()->SetTitle("Position (cm)");
    hist_up->GetYaxis()->SetTitle("Count");
    hist_up->GetXaxis()->CenterTitle();
    hist_up->GetYaxis()->CenterTitle();
    hist_up->GetXaxis()->SetLabelSize(0.05);
    hist_up->GetYaxis()->SetLabelSize(0.05);
    hist_up->GetXaxis()->SetTitleSize(0.05);
    hist_up->GetYaxis()->SetTitleSize(0.05);

    auto legend = new TLegend();
    legend->AddEntry(hist_up, "TAC UP");
    legend->AddEntry(hist_down, "TAC DOWN");
    legend->Draw();
}


void plot_position_calibration_peaks() {
    TH1D *hist_up = getHistoWithFilterFromChannelWithCalibration(
        "files/overnight_after_fix_coinc_remapping.root", "", 400, 0, 1.5, 1, 3, 5000, 10000,
        0.00010914992943457062, -0.7429201535521206
    );
    TH1D *hist_down = getHistoWithFilterFromChannelWithCalibration(
        "files/overnight_after_fix_coinc_remapping.root", "", 400, 0, 1.5, 2, 3, 5000, 10000,
        0.0001066245854969239, -1.1976638553317625
    );

    hist_up->SetStats(0);
    hist_down->SetStats(0);

    hist_up->SetLineColor(4);
    hist_down->SetLineColor(2);

    auto c1 = new TCanvas("c1","c1",0,0,700,600);
    c1->SetGrid();
    gStyle->SetPadLeftMargin(0.12);

    hist_up->GetYaxis()->SetRangeUser(0., 60.);
    hist_down->GetYaxis()->SetRangeUser(0., 60.);

    hist_up->Draw();
    hist_down->Draw("same");

    hist_up->SetLineWidth(2);
    hist_down->SetLineWidth(2);

    hist_up->SetTitle("");
    hist_up->GetXaxis()->SetTitle("Position (cm)");
    hist_up->GetYaxis()->SetTitle("Count");
    hist_up->GetXaxis()->CenterTitle();
    hist_up->GetYaxis()->CenterTitle();
    hist_up->GetXaxis()->SetLabelSize(0.05);
    hist_up->GetYaxis()->SetLabelSize(0.05);
    hist_up->GetXaxis()->SetTitleSize(0.05);
    hist_up->GetYaxis()->SetTitleSize(0.05);

    auto legend = new TLegend();
    legend->AddEntry(hist_up, "TAC UP");
    legend->AddEntry(hist_down, "TAC DOWN");
    legend->Draw();
}
