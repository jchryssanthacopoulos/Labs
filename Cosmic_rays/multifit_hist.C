
void multifit(TH1D *hist) {
   // TF1 *g1 = new TF1("g1", "gaus+pol1(3)", 7, 15);
   // TF1 *g2 = new TF1("g2", "gaus+pol1(3)", 18, 25);
   TF1 *g1 = new TF1("g1", "gaus+pol1(3)", 9, 15);
   TF1 *g2 = new TF1("g2", "gaus+pol1(3)", 20, 25);

   Double_t par1[5] = {42, 11, 1.4, 0, 0};
   Double_t par2[5] = {37, 22, 1.6, 0, 0};

   g1->SetParameters(par1);
   g2->SetParameters(par2);

   hist->Fit(g1, "R");
   hist->Fit(g2, "R+");

   hist->SetStats(0);
   hist->Draw();
}
