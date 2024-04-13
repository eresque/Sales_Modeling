import React, { useState } from 'react';
import classNames from 'classnames';
import './style.scss';

type InputChoiceProps = {
    className: string,
    setModel: React.Dispatch<React.SetStateAction<string>>
    style?: React.CSSProperties
};

const InputChoice = (props: InputChoiceProps): JSX.Element => {
    const [value, setValue] = useState<string>('');
    const arOptions: Array<string> = ['XGBoost'];

    const options = arOptions.map((text, index) => {
        return <option key={index} value={text}>{text}</option>;
    });

    const onChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setValue(event.target.value);
        props.setModel(event.target.value);
    }

    const classes = classNames(
        'input-choice ' + props.className,
    );

    return (
        <select className={classes} value={value} onChange={onChange}>
            <option value="" hidden disabled>Модель</option>
            {options}
        </select>
    );
}

InputChoice.defaultProps = {
    className: 'input-choice',
    style: {}
};

export default InputChoice;