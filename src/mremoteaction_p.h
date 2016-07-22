/***************************************************************************
**
** Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
** All rights reserved.
** Contact: Nokia Corporation (directui@nokia.com)
**
** This file is part of libmeegotouch.
**
** If you have questions regarding the use of this file, please contact
** Nokia at directui@nokia.com.
**
** This library is free software; you can redistribute it and/or
** modify it under the terms of the GNU Lesser General Public
** License version 2.1 as published by the Free Software Foundation
** and appearing in the file LICENSE.LGPL included in the packaging
** of this file.
**
****************************************************************************/

#ifndef MREMOTEACTION_P_H
#define MREMOTEACTION_P_H

#include <QObject>
#include <QProcess>
#include <QString>
#include <QVariant>
#include <QVector>

class MRemoteAction;

class MRemoteActionPrivate
{
    Q_DECLARE_PUBLIC(MRemoteAction)

public:
    MRemoteActionPrivate();
    virtual ~MRemoteActionPrivate();

    //! The name of the D-Bus service to call
    QString serviceName;
    //! The path of the D-Bus object to call
    QString objectPath;
    //! The name of the D-Bus interface to call
    QString interface;
    //! The name of the D-Bus method to call
    QString methodName;
    //! The arguments of the D-Bus call
    QList<QVariant> arguments;

protected:
    MRemoteAction *q_ptr;
};

class MRemoteActionUnprivilegedInvoker : public QProcess
{
    Q_OBJECT
public:
    MRemoteActionUnprivilegedInvoker(QObject *parent = 0);
    ~MRemoteActionUnprivilegedInvoker();

    Q_INVOKABLE void invoke(const MRemoteAction &action);

protected:
    void setupChildProcess() override;

private:
    void invokeNextCall(int code, ExitStatus status);

    QStringList m_queuedCalls;
};

#endif
