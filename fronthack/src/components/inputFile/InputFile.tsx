import { useState, useRef } from 'react';
import './style.scss';
import Button from '../button/Button';

type InputFileProps = {
    text: string,
    setFile: React.Dispatch<React.SetStateAction<File | undefined>>,
    children: React.ReactNode,
    style?: React.CSSProperties
};

const InputFile = (props: InputFileProps) => {
    const filePicker = useRef(null);
    const [fileName, setFileName] = useState<string>('');

    const handlePick = () => {
        const picker: any = filePicker.current;
        picker.click();
    };

    const handleChange = (event: React.ChangeEvent) => {
        const target = event.target as HTMLInputElement;
        const file: File = (target.files as FileList)[0];
        props.setFile(file);

        if (file.name.length <= 20) {
            setFileName(file.name);
        }
        else {
            let res = file.name.slice(0, 13) + '...' + file.name.slice(-4);
            setFileName(res);
        }
    };

    return (
        <>
            <Button className="btn-file" type="button" onClick={handlePick} text={fileName == '' ? props.text : fileName}>
                {props.children}
            </Button>
            <input
                type="file"
                id="input-files"
                name="files"
                ref={filePicker}
                onChange={handleChange}
                accept=".csv"
            />
        </>
    );
};

export default InputFile;