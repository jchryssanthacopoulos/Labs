//Digitizer data from the LAB

struct slimport_data_t {
	ULong64_t	timetag; //time stamp
	UInt_t		baseline;
	UShort_t	qshort; //integration with shorter time
	UShort_t	qlong; //integration with longer time
	UShort_t	pur;
	UShort_t	samples[4096];
};

TH1D* getHistoFromTree(const char *name_file, int numBins, double minX, double maxX) {
	// variables
	slimport_data_t indata;
	TFile *infile = new TFile(name_file);
	TTree *intree = (TTree*)infile->Get("acq_tree_0");
	TBranch *inbranch = intree->GetBranch("acq_ch0");
	inbranch->SetAddress(&indata.timetag);
	TH1D *h_spectrum = new TH1D("h_spectrum","Total spectrum",numBins,minX,maxX);
	// histogram filling
	for (int i=0; i<inbranch->GetEntries(); i++) {
		inbranch->GetEntry(i);
		h_spectrum->Fill(indata.qlong);
	}
	// return
	return h_spectrum;
}

TH1D* getHistoForChannelFromTree(const char *name_file, short chan, int numBins, double minX, double maxX) {
	// variables
	slimport_data_t indata;
	TFile *infile = new TFile(name_file);
	TTree *intree = (TTree*)infile->Get("acq_tree_0");
	TBranch *inbranch = intree->GetBranch(Form("acq_ch%d",chan));
	inbranch->SetAddress(&indata.timetag);
	TH1D *h_spectrum = new TH1D("h_spectrum","Total spectrum",numBins,minX,maxX);
	// histogram filling
	for (int i=0; i<inbranch->GetEntries(); i++) {
		inbranch->GetEntry(i);
		h_spectrum->Fill(indata.qlong);
	}
	// return
	return h_spectrum;
}


TH1D* getHistoWithFilter(const char *name_file, int numBins, double minX, double maxX, double lowThr = 0, double highThr = 999999) {
	// variables
	slimport_data_t indata;
	TFile *infile = new TFile(name_file);
	TTree *intree = (TTree*)infile->Get("acq_tree_0");
	TBranch *inbranch = intree->GetBranch("acq_ch0");
	inbranch->SetAddress(&indata.timetag);
	TH1D *h_spectrum = new TH1D("h_spectrum","Total spectrum",numBins,minX,maxX);
	// histogram filling
	for (int i=0; i<inbranch->GetEntries(); i++) {
		inbranch->GetEntry(i);
		if (indata.qlong>lowThr && indata.qlong<highThr) {
			h_spectrum->Fill(indata.qlong);
		}
	}
	// return
	return h_spectrum;
}


TGraph *getSignal(const char *name_file, int nSamples=250, short chan=0, int nrEv=1){
	// variables
	slimport_data_t indata;
	TFile *infile = new TFile(name_file);
	TTree *intree = (TTree*)infile->Get("acq_tree_0");
	TBranch *inbranch = intree->GetBranch(Form("acq_ch%d",chan));
	inbranch->SetAddress(&indata.timetag);
	TGraph *graph = new TGraph();
	
	//Setting the desired event
	inbranch->GetEntry(nrEv);

	//Looping over the samples
	for (int i=0; i<nSamples; ++i){
		graph->SetPoint(i, i, indata.samples[i]);
	}
	return graph;
}


TH1D* getHistoWithFilterFromChannel(const char *name_file, int numBins, double minX, double maxX, short chan1, short chan2, double thres1, double thres2) {
	// variables
	slimport_data_t indata1, indata2;
	TFile *infile = new TFile(name_file);
	TTree *intree = (TTree*)infile->Get("acq_tree_0");
	TBranch *inbranch1 = intree->GetBranch(Form("acq_ch%d",chan1));
	TBranch *inbranch2 = intree->GetBranch(Form("acq_ch%d",chan2));
	inbranch1->SetAddress(&indata1.timetag);
	inbranch2->SetAddress(&indata2.timetag);
	TH1D *h_spectrum = new TH1D("h_spectrum","Total spectrum",numBins,minX,maxX);
	// histogram filling
	for (int i=0; i<inbranch1->GetEntries(); i++) {
		inbranch1->GetEntry(i);
		inbranch2->GetEntry(i);
		if (indata2.qlong>thres1 && indata2.qlong<thres2) {
			h_spectrum->Fill(indata1.qlong);
		}
	}
	// return
	return h_spectrum;
}
