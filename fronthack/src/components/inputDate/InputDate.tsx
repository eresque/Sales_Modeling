import React from 'react';
import classNames from 'classnames';
import './style.scss';

type InputDateProps = {
    value: string | Array<string>,
    onChange?: React.ChangeEventHandler<HTMLInputElement>,
    className: string,
    placeholder?: string,
    style?: React.CSSProperties
};

const InputDate = (props: InputDateProps): JSX.Element => {

    const classes = classNames(
        'input-date ' + props.className,
    );

    return (
        <input
            name={props.className}
            className={classes}
            placeholder={props.placeholder}
            value={props.value}
            onChange={props.onChange}
            style={props.style}
            type='date'
        />
    );
};

InputDate.defaultProps = {
    value: '',
    onChange: () => { },
    className: 'input-date',
    placeholder: '',
    style: {}
};

export default InputDate;