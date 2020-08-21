{
// Reads the XRF MCA text file and fills a calibrated MCA histogram
// Change the input and output file names in line 23-24
gROOT->Reset();

ifstream spectrum;
ofstream spectrout;
char buf[128],filename[128],fileout[128];
std::string LineBuffer;

Int_t i,j,k, ncal=0;
Float_t tFalue;
Float_t ch[5], E[5];
Float_t ltm;

bool ConfigRead = true;
bool EndRead = false;
bool DataRead = false;

int bin0 = 785;	//783;
int bin1 = 829;	//829;
const int numbins = 4096;

// **************************** //
// Filename business
// **************************** //

//sprintf(filename,"C:/KLASSE/Fis384/XRF_data2019/Cr_tgt.mca");	// 01_MT
//sprintf(fileout, "C:/KLASSE/Fis384/XRF_data2019/Cr_tgt.root"); //C:\KLASSE\Fis384\2018\hns_grp2\hns
//sprintf(filename,"C:/KLASSE/Fis384/2018/hns_grp2/hns/10_124Sn.mca");	// 12_116Sn, 09_I0  03_MT_Cu
//sprintf(fileout, "C:/KLASSE/Fis384/2018/hns_grp2/hns/10_124Sn.root"); //C:\KLASSE\Fis384\2018\hns_grp2\hns
sprintf(filename,"C:/KLASSE/Fis384/XRF_data2019/Cr_tgt_gr1.mca");	//   04_Cu_Cr_tgt4, 03_MT_Cu, 01_MT_gr1
sprintf(fileout, "C:/KLASSE/Fis384/XRF_data2019/Cr_tgt_gr1.root"); //

// ********************************************************************* //
// define the histograms
// ********************************************************************* //

TH1F *h1 = new TH1F("h1",";Channel;counts [arb. units]",numbins,0,numbins);

// ********************************************************************* //
// unpack the mca file
// ********************************************************************* //

// open the file
spectrum.open(filename);

if(spectrum.is_open()){
	cout << "starts mca conversion" << endl;
	cout << " input: " << filename << "\n output: " << fileout << endl;
	while(! spectrum.eof()){
		spectrum >> LineBuffer;
//			if(LineBuffer.compare(0,9,"LIVE_TIME") == 0) {	// for root v6?
			if(LineBuffer.compare("LIVE_TIME") == 0) {
				  spectrum >> LineBuffer;
				  spectrum >> LineBuffer;
				  ltm = atof(LineBuffer.c_str());
				  printf("Live Time: %f \n",ltm);
			}
//			else if(LineBuffer.compare(0,15,"<<CALIBRATION>>") == 0) {
			else if(LineBuffer.compare("<<CALIBRATION>>") == 0) {
				  spectrum >> LineBuffer;
				  spectrum >> LineBuffer;
				  spectrum >> LineBuffer;
				  spectrum >> LineBuffer;
				  ch[0] = atof(LineBuffer.c_str());
				  printf("ch0: %f \n",ch[0]);
				  spectrum >> LineBuffer;
				  E[0] = atof(LineBuffer.c_str());
				  printf("E0: %f \n",E[0]);
				  spectrum >> LineBuffer;
				  ch[1] = atof(LineBuffer.c_str());
				  printf("ch1: %f \n",ch[1]);
				  spectrum >> LineBuffer;
				  E[1] = atof(LineBuffer.c_str());
				  printf("E1: %f \n",E[1]);
				  ncal=2;
				  spectrum >> LineBuffer;
				  if(LineBuffer.compare("<<ROI>>") == 0) continue;
				  else {
				  	ch[2] = atof(LineBuffer.c_str());
				  	printf("ch2: %f \n",ch[2]);
				  	spectrum >> LineBuffer;
				  	E[2] = atof(LineBuffer.c_str());
				  	printf("E2: %f \n",E[2]);
				  	ncal=3;
				  }
			}
			else if(LineBuffer.compare("<<END>>") == 0) {
				  DataRead = false;
//				  EndRead = true;
				  printf("Total data read: %d \n",i);
				  break;
			}
			else if(DataRead) {
				  h1->SetBinContent(i,atof(LineBuffer.c_str())/ltm);
				  i++;
			}
//			else if(LineBuffer.compare(0,8,"<<DATA>>") == 0) {
			else if(LineBuffer.compare("<<DATA>>") == 0) {
				  DataRead = true;python integrate array

TGraph *gr = new TGraph(ncal,X,Y);
gr->Draw("A*");
gr->Fit("pol1");
Double_t *par;
par = pol1->GetParameters();
// p0 = -0.006083 and p1 = 0.00997
cout<<"p0: "<<par[0]<<", p1: "<<par[1]<<endl;

// ********************************************************************* //
// filling histograms
// ********************************************************************* //

TH1F *h2 = new TH1F("h2",";E [keV];counts per second [s-1]",numbins,0*par[1]+par[0],numbins*par[1]+par[0]);

for(j=0;j<numbins;j++) {
	h2->SetBinContent(j,h1->GetBinContent(j));
}

h1->Draw();
h2->Draw();
//h1->Draw();
Float_t area = h2->Integral(bin0,bin1);
cout<<"Integral: "<<area<<" cps"<<endl;


// ********************************************************************* //
// write the histograms in a root output file for further processing
// ********************************************************************* //

	TFile *file2 = new TFile(fileout,"RECREATE");
	h1->Write();
	h2->Write();
	gr->Write();
	file2->Close();
// read again with : TFile _file0("01_MT.root")
// The usual TFile *_file0 = TFile::Open("01_MT.root") does not seem to work ...??

// ********************************************************************* //
// Close all files to exit cleanly
// ********************************************************************* //

	spectrum.close();

// 01_MT: 4468 cps
// 02_MT: 4465 cps
// Cr_tgt: 3262 cps



} // finish en klaar

