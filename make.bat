
rem Con esta línea le estamos diciendo que tiene que empezar por la función main
rem With this line we are telling you that you have to start with the main function
@echo off&cls&call:main %1&goto:EOF

:main
    rem Ckequeando parámetros
    if [%1]==[] (call :compile)
    if [%1]==[create] (call :compile)
    if [%1]==[win] (call :win)
    if [%1]==[pdf] (call :pdf)
    if [%1]==[exe] (call :exe)
    if [%1]==[clean] (call :clean)
    rem Si el argumento no está vacío, ni es compile, ni es clear, etc
    if [%1] NEQ [] (
        if [%1] NEQ [compile] ( 
            if [%1] NEQ [win] (
                if [%1] NEQ [pdf] (
                    if [%1] NEQ [exe] (
                        if [%1] NEQ [clean] ( 
                            if [%1] NEQ [help] (
                                if [%1] NEQ [clean] (call :help) 
                            }
                        }
                    }
                }
            }
        )
    )    
goto:eof

:help
     echo No reconozco la sintaxis, pon:
     echo .
     echo make [] [compile] [clear] [help] 
goto:eof

:clean
    echo escogiste borrar
    rmdir /S /Q build
    rmdir /S /Q dist
    del /F /Q "*.spec"
    del /F /Q "*.pdf"
    del /F /Q "*.doc"
    del /F /Q "*.docx"
goto:eof

:exe
     echo vamos a crear el ejecutable para windows
     rem pyinstaller --windowed --onefile --icon=./data/icon.ico word2pdf.py
     pyinstaller --onefile --icon=./data/icon.ico word2pdf.py
goto:eof

:compile
    echo "Vamos a convertir test.docx en pdf"
    word2pdf.py data\test.docx
    move data\test.pdf .\
goto:eof

:win
    word2pdf.py
goto:eof


:pdf
    echo "Vamos a convertir kotlin.pdf a docx"
    word2pdf.py data\test.pdf
    move data\test.docx .\
goto:eof

