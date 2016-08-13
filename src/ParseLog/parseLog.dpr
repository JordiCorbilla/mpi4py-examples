program parseLog;

uses
  Vcl.Forms,
  thundax.parselog in 'thundax.parselog.pas' {Form1},
  Vcl.Themes,
  Vcl.Styles;

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  TStyleManager.TrySetStyle('Slate Classico');
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
