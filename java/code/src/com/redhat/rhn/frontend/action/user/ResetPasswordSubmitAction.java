/**
 * Copyright (c) 2015 Red Hat, Inc.
 *
 * This software is licensed to you under the GNU General Public License,
 * version 2 (GPLv2). There is NO WARRANTY for this software, express or
 * implied, including the implied warranties of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
 * along with this software; if not, see
 * http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
 *
 * Red Hat trademarks are not licensed under GPLv2. No permission is
 * granted to use or replicate Red Hat trademarks that are incorporated
 * in this software or its documentation.
 */
package com.redhat.rhn.frontend.action.user;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.log4j.Logger;
import org.apache.struts.action.ActionErrors;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionForward;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.ActionMessage;
import org.apache.struts.action.ActionMessages;
import org.apache.struts.action.DynaActionForm;

import com.redhat.rhn.common.db.ResetPasswordFactory;
import com.redhat.rhn.domain.user.User;
import com.redhat.rhn.frontend.struts.RequestContext;
import com.redhat.rhn.frontend.struts.RhnAction;
import com.redhat.rhn.manager.user.UserManager;

/**
 * ResetPasswordSubmitAction, responds to user pushing 'update' on the change-password
 * form
 *
 * @version $Rev: $
 */
public class ResetPasswordSubmitAction extends RhnAction {

    private static Logger log = Logger.getLogger(ResetPasswordSubmitAction.class);

    @Override
    public ActionForward execute(ActionMapping mapping, ActionForm formIn,
                    HttpServletRequest request, HttpServletResponse response) {

        log.error("ResetPasswordSubmitAction");
        DynaActionForm form = (DynaActionForm) formIn;
        RequestContext requestContext = new RequestContext(request);
        User user = requestContext.getCurrentUser();

        ActionErrors errors = new ActionErrors();

        // Add an error in case of password mismatch
        String pw = (String) form.get("password");
        String conf = (String) form.get("passwordConfirm");
        if (!pw.equals(conf)) {
            errors.add(ActionMessages.GLOBAL_MESSAGE, new ActionMessage(
                       "error.password_mismatch"));
            return mapping.findForward("failure");
        }

        // If there are no errors, store the user and return the success mapping
        user.setPassword(pw);
        UserManager.storeUser(user);
        ResetPasswordFactory.invalidateUserTokens(user.getId());

        ActionMessages msgs = new ActionMessages();
        msgs.add(ActionMessages.GLOBAL_MESSAGE,
                 new ActionMessage("message.userInfoUpdated"));
        getStrutsDelegate().saveMessages(request, msgs);
        return mapping.findForward("success");
    }

}