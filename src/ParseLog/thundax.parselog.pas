// Copyright (c) 2016, Jordi Corbilla
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// - Redistributions of source code must retain the above copyright notice,
// this list of conditions and the following disclaimer.
// - Redistributions in binary form must reproduce the above copyright notice,
// this list of conditions and the following disclaimer in the documentation
// and/or other materials provided with the distribution.
// - Neither the name of this library nor the names of its contributors may be
// used to endorse or promote products derived from this software without
// specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.

unit thundax.parselog;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Vcl.ComCtrls, Vcl.Grids;

type
  TForm1 = class(TForm)
    PageControl1: TPageControl;
    TabSheet1: TTabSheet;
    TabSheet2: TTabSheet;
    Memo2: TMemo;
    log: TMemo;
    Button1: TButton;
    Button2: TButton;
    Memo1: TMemo;
    StringGrid1: TStringGrid;
    Button3: TButton;
    Button4: TButton;
    Copy: TButton;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure CopyClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

uses
  System.StrUtils, ClipBrd;

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
var
  i: Integer;
  s : string;
  flag : boolean;
  date : string;
  counter : integer;
  flagcontains : boolean;
  cpu1, cpu2, cpu3, cpu4 : string;
begin
  counter := 1;
  flagcontains := false;
  flag := false;
  for i := 0 to memo2.Lines.Count-1 do
  begin
    s := memo2.Lines[i];

    if flag then
    begin
      //flagcontains := false;
      if s.Contains('python') then
      begin
        flagcontains := true;
        if counter = 1 then
          cpu1 := s.Substring(0,5).trim()
        else if counter = 2 then
          cpu2 := s.Substring(0,5).trim()
        else if counter = 3 then
          cpu3 := s.Substring(0,5).trim()
        else if counter = 4 then
        begin
          cpu4 := s.Substring(0,5).trim()
        end;
        counter := counter + 1;
        if counter = 5 then
          log.Lines.Add(date + ' , ' + cpu1+ ', ' + cpu2+ ', ' + cpu3+ ', ' + cpu4);
      end;
    end;

    if s.Contains('%CPU %MEM') then
    begin
      if (not flagcontains and flag) then
      begin
        log.Lines.Add(date + ' , 0.0, 0.0, 0.0, 0.0');
      end;
      if counter > 4 then
      begin
        counter := 1;
        flagcontains := false;
      end;
      flag := true;
      date := s;
      date := date.Replace('%CPU %MEM ARGS Fri 12 Aug ', '');
      date := date.Replace(' UTC 2016', '');
    end;


  end;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  log.Lines.Clear;
end;

procedure TForm1.Button3Click(Sender: TObject);
var
  i: Integer;
  s : string;
  start : boolean;
  process : string;
  time : string;
  test : integer;
  column : integer;
begin
  //Process each line
  test := 1;
  start := false;
  for i := 0 to memo1.Lines.Count-1 do
  begin
    s := memo1.Lines[i];

    if start then
    begin
      //Process 3 finished in 0.0018s.
      if s.Contains('Process') then
      begin
        //Process 3 finished in 0.0018s.
        s := s.Replace('Process ', '');
        //3 finished in 0.0018s.
        process := AnsiLeftStr(s, AnsiPos(' ', s));
        //finished in 0.0018s.
        s := AnsiRightStr(s, length(s) - length(process));
        s := s.Replace('finished in ', '');
        time := s.Replace('s.', '');
        process := process.Replace(' ', '');
        column := process.ToInteger();
        StringGrid1.Cells[column, test] := time;
      end;
    end;

    if s.Contains('Start') then
      start := true;

    if s.Contains('End') then
    begin
      start := false;
      test := test + 1;
    end;
  end;
end;

procedure TForm1.Button4Click(Sender: TObject);
var
  I: Integer;
  j: Integer;
begin
  for I := 1 to 12 do
  begin
    StringGrid1.Cells[i, 0] := i.ToString();
  end;

  for I := 1 to 10 do
  begin
    StringGrid1.Cells[0, i] := i.ToString();
  end;

  for i := 1 to 10 do
  begin
    for j := 1 to 12 do
      StringGrid1.Cells[j, i] := '';
  end;
  memo1.Lines.Clear;
end;

procedure TForm1.CopyClick(Sender: TObject);
var
  S: string;
  i, j: Integer;
begin
  S := '';
  for j := StringGrid1.Selection.Top to StringGrid1.Selection.Bottom do
  begin
    for i := StringGrid1.Selection.Left to StringGrid1.Selection.Right - 1 do
      S := S + StringGrid1.Cells[i, j] + #9;
    S := S + StringGrid1.Cells[StringGrid1.Selection.Right, j] + sLineBreak;
  end;
  Delete(S, Length(S) - Length(sLineBreak) + 1, Length(sLineBreak));
  Clipboard.AsText := S;
end;

procedure TForm1.FormCreate(Sender: TObject);
begin
  Button2Click(sender);
  Button4Click(sender);
end;

end.
